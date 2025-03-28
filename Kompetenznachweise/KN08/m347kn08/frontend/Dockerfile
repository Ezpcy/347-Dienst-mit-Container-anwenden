FROM node:latest AS prod

WORKDIR /app

COPY app/package.json /app

RUN npm install

COPY ./app /app

RUN npm run build

FROM nginx  
WORKDIR /usr/local/bin

COPY gen-conf.sh .

COPY --from=prod app/build/ /usr/share/nginx/html

COPY custom-nginx.template /etc/nginx/conf.d/custom-nginx.template
COPY env.sh /docker-entrypoint.d/env.sh

RUN chmod +x /docker-entrypoint.d/env.sh
RUN chmod +x gen-conf.sh

EXPOSE 	80
ENTRYPOINT [ "/bin/sh", "gen-conf.sh" ]
