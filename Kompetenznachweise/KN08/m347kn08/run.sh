#!/bin/bash

docker build -t ezpcy/m347:kn08account ./account/
docker run -d --name account -p 8080:8080 ezpcy/m347:kn08account

docker build -t ezpcy/m347:kn08front ./frontend/
docker run -d \
        -p 8060:80 \
        --name frontend-container \
        -e FRONTEND_MS_ACCOUNT_HOLDINGS="http://localhost:8080/Account/Cryptos/?userid=<userId>" \
        -e FRONTEND_MS_ACCOUNT_FRIENDS="http://localhost:8080/Account/Friends/?userid=<userId>" \
        -e FRONTEND_MS_BUYSELL_BUY="http://localhost:8002/buy" \
        -e FRONTEND_MS_BUYSELL_SELL="http://localhost:8002/sell" \
        -e FRONTEND_MS_SENDRECEIVE_SEND="http://localhost:8003/send" \
        -e FRONTEND_MS_USER_LOGGED_IN="1" \
        ezpcy/m347:kn08front

docker build -t ezpcy/m347:kn08buysellmicro ./microservice/buysell/
docker run -d --name buysell -p 8002:8002 -e ACCOUNT_SERVICE_URL="http://host.docker.internal:8080" ezpcy/m347:kn08buysellmicro

docker build -t ezpcy/m347:kn08sendreceivemicro ./microservice/sendreceive/
docker run -d --name sendreceive -p 8003:8003 -e ACCOUNT_SERVICE_URL="http://host.docker.internal:8080" ezpcy/m347:kn08sendreceivemicro
