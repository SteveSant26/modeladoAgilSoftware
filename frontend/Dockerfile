# Paso 1: Construir la app Angular
FROM node:18 AS builder

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del frontend al contenedor
COPY . .

# Instalar dependencias y compilar la app en modo producción
RUN npm install
RUN npm run build -- --configuration production

# Paso 2: Servir la app compilada con NGINX
FROM nginx:alpine

# (Opcional) Copia configuración personalizada de NGINX si la tienes
COPY nginx.conf /etc/nginx/nginx.conf

# Copia el resultado del build Angular al directorio que sirve NGINX
COPY --from=builder /app/dist/frontend/browser /usr/share/nginx/html

# Expone el puerto que usará Cloud Run
EXPOSE 8080

# Comando por defecto para iniciar NGINX
CMD ["nginx", "-g", "daemon off;"]
