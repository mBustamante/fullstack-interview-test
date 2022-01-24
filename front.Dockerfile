FROM node:14-alpine
WORKDIR /app/frontend

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080
