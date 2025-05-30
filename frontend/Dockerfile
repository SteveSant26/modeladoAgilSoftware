# Paso 1: Construir la app Angular
FROM node:18 AS builder

WORKDIR /app
COPY frontend/ ./

# Instalar dependencias y compilar
RUN npm install
RUN npm run build -- --configuration production

# Paso 2: Crear contenedor final con NGINX
FROM nginx:alpine

# Copiar archivo de configuración personalizado (opcional)
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar archivos Angular compilados al servidor NGINX
COPY --from=builder /app/dist/frontend/browser /usr/share/nginx/html

# Exponer el puerto 80 (necesario para Cloud Run)
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
