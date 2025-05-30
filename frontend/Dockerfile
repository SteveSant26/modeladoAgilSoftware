# Paso 1: Construir la app Angular
FROM node:18-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli
RUN npm install
RUN ng build --configuration=production

# Paso 2: Servir con http-server
FROM node:18-alpine
WORKDIR /app
RUN npm install -g http-server
COPY --from=builder /app/dist/* /app
CMD ["http-server", "frontend", "-p", "8080"]
