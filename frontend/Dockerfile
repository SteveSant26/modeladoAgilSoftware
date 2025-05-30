FROM node:alpine
WORKDIR /usr/src/app
COPY . .
RUN npm install -g @angular/cli
RUN npm install
CMD ["sh", "-c", "ng serve --host 0.0.0.0 --port ${PORT}"]
