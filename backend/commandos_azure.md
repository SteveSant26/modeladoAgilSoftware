az login
az provider register --namespace Microsoft.Compute --wait
az provider register --namespace Microsoft.Network --wait


## creación de ssh key
ssh-keygen -t rsa -b 2048