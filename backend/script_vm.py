import os
from dotenv import load_dotenv
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

# Cargar variables de entorno
load_dotenv()
SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
SSH_KEY = os.getenv("AZURE_SSH_KEY")

# Configuración general
RESOURCE_GROUP_NAME = "VM-Azure-group"
LOCATION = "eastus"
VM_NAME = "Vm-Azure"
USERNAME = "StevenSant"

# Autenticación
credential = InteractiveBrowserCredential()

# Clientes
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)
network_client = NetworkManagementClient(credential, SUBSCRIPTION_ID)

# ------------------ FUNCIONES ------------------


def create_group_recurses():
    print("Creando grupo de recursos...")
    rg_result = resource_client.resource_groups.create_or_update(
        RESOURCE_GROUP_NAME,
        {
            "location": LOCATION,
            "tags": {"enviroment": "development", "project": "web_app"},
        },
    )
    print(f"Grupo de recursos creado: {rg_result.name}")
    return rg_result


def setup_network():
    print("Configurando red virtual y subred...")
    vnet = network_client.virtual_networks.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        "miVNet",
        {"location": LOCATION, "address_space": {"address_prefixes": ["10.0.0.0/16"]}},
    ).result()

    subnet = network_client.subnets.begin_create_or_update(
        RESOURCE_GROUP_NAME, "miVNet", "miSubred", {"address_prefix": "10.0.0.0/24"}
    ).result()

    return vnet, subnet


def create_public_ip():
    print("Creando IP pública...")
    ip = network_client.public_ip_addresses.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        "miPublicIP",
        {
            "location": LOCATION,
            "sku": {"name": "Basic"},
            "public_ip_allocation_method": "Static",
        },
    ).result()
    return ip


def create_nic(subnet, ip_address):
    print("Creando interfaz de red...")
    nic = network_client.network_interfaces.begin_create_or_update(
        RESOURCE_GROUP_NAME,
        "miNIC",
        {
            "location": LOCATION,
            "ip_configurations": [
                {
                    "name": "miIPconfig",
                    "subnet": {"id": subnet.id},
                    "public_ip_address": {"id": ip_address.id},
                }
            ],
        },
    ).result()
    return nic


def define_os_profile():
    print("Configurando perfil del sistema operativo...")
    return {
        "computer_name": VM_NAME,
        "admin_username": USERNAME,
        "linux_configuration": {
            "disable_password_authentication": True,
            "ssh": {
                "public_keys": [
                    {
                        "path": f"/home/{USERNAME}/.ssh/authorized_keys",
                        "key_data": SSH_KEY.strip(),
                    }
                ]
            },
        },
    }


def create_vm(nic, os_profile):
    print("Iniciando creación de VM...")
    vm_parameters = {
        "location": LOCATION,
        "storage_profile": {
            "image_reference": {
                "publisher": "Canonical",
                "offer": "0001-com-ubuntu-server-jammy",
                "sku": "22_04-lts",
                "version": "latest",
            },
            "os_disk": {
                "name": f"{VM_NAME}-osdisk",
                "caching": "ReadWrite",
                "create_option": "FromImage",
                "managed_disk": {"storage_account_type": "StandardSSD_LRS"},
            },
        },
        "hardware_profile": {"vm_size": "Standard_B1s"},
        "os_profile": os_profile,
        "network_profile": {"network_interfaces": [{"id": nic.id}]},
    }

    vm_poller = compute_client.virtual_machines.begin_create_or_update(
        RESOURCE_GROUP_NAME, VM_NAME, vm_parameters
    )
    return vm_poller.result()


# ------------------ EJECUCIÓN ------------------


def main():
    create_group_recurses()
    _, subnet = setup_network()
    ip_address = create_public_ip()
    nic = create_nic(subnet, ip_address)
    os_profile = define_os_profile()
    vm = create_vm(nic, os_profile)

    print(f"\nMáquina virtual '{VM_NAME}' creada exitosamente!")
    print(f"IP pública: {ip_address.ip_address}")
    print(f"Conéctate usando: ssh {USERNAME}@{ip_address.ip_address}")


if __name__ == "__main__":
    main()
