FROM node:18

WORKDIR /app

COPY package.json .

RUN npm install

COPY app.js .

EXPOSE 8200

CMD ["node", "app.js"]
