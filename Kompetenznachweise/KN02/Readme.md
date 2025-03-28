# KN02: Dockerfile

## Dockerfile I

```dockerfile
FROM nginx 
COPY static-html-directory /var/www/html 
EXPOSE 	80
```

**Dockerfile für das Repository:**

```dockerfile
FROM nginx
WORKDIR /usr/share/nginx/html
COPY static/index.html .
EXPOSE 80
```

**Ausgeführte Befehle:**

```bash
docker build -t ezpcy/m346:kn02a .
docker run -d -p 8080:80 ezpcy/m347:kn02a
docker push ezpcy/m346:kn02a
```

![](image/Pasted%20image%2020250221105029.png)

_Abbildung 1: Dockerfile_

![](image/Pasted%20image%2020250221105218.png)

_Abbildung 2: Webseite_

## Dockerfile II

### MariaDB

```dockerfile
FROM mariadb:latest

ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=pw
ENV MYSQL_ROOT_PASSWORD=rootpw
ENV MYSQL_DATABASE=mysql

EXPOSE 3306
```

Befehle:

```bash
docker build -t ezpcy/m346:kn02b-db .
docker run -d -p 3306:3306 ezpcy/m346:kn02b-db
docker push ezpcy/m346:kn02b-db
```

![](image/Pasted%20image%2020250221113107.png)

_Abbildung 3: Telnet zugriff auf den Datenbank Port_

### Apache

```dockerfile
FROM php:8.0-apache

WORKDIR /var/www/html
RUN docker-php-ext-install mysqli
EXPOSE 80

COPY . .
```

Befehle:

```bash
docker build -t ezpcy/m346:kn02b-web .
docker run -d -p 8080:80 ezpcy/m346:kn02b-web
docker push ezpcy/m346:kn02b-web
```

### Docker Netzwerk

Befehle zum erstellen des Netzwerks:

```bash
docker network create kn02b-net
docker network connect kn02b-net kn02b-db
docker network connect kn02b-net kn02b-web
```

Oder im `docker run` Befehl`:

```bash
docker run -d -p 8080:80 --network kn02b-net ezpcy/m346:kn02b-web
docker run -d -p 3306:3306 --network kn02b-net ezpcy/m346:kn02b-db
```

![](image/Pasted%20image%2020250221113938.png)

_Abbildung 4: `db.php`_

![](image/Pasted%20image%2020250221114010.png)

_Abbildung 5: `info.php`_
