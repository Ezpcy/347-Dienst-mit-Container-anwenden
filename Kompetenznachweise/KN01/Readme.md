# KN01: Docker Grundlagen

## Installation

`docker/getting-started` Repository:

```bash
docker pull docker/getting-started
```

Ausführen des Containers:

```bash
docker run -d -p 8080:8080 docker/getting-started
```

### Webseite

![](image/Pasted%20image%2020250221092712.png)
*Abbildung 1: Getting started Webseite*

### Container

![](image/Pasted%20image%2020250221092755.png)
*Abbildung 2: Docker Container*

## Docker Command Line Interface

-  Docker Version anzeigen:

```bash
docker version
```

- Docker search `ubuntu`und `nginx`:

```bash
docker search ubuntu
docker search nginx
```

![](image/Pasted%20image%2020250221093131.png)
*Abbildung 3: Docker Search Befehl*

-  Docker Befehl `dokcer rund -d -p 80:80 docker/getting-started` erklärt:
	- `-d`: Bedeutet, dass der Container im Hintergrund ausgeführt wird.
	- `-p`: Portweiterleitung vom Host auf den Container.
	- `80:80`: Port 80 auf dem Host wird auf Port 80 im Container weitergeleitet.
	- `docker/getting-started`: Name des Images.

-  `nginx` Container erstellen:

```bash
docker pull nginx
docker create --name nginx -p 8081:80 nginx
docker start nginx
```

![](image/Pasted%20image%2020250221093718.png)
*Abbildung 4: Nginx Webseite*

-  `ubuntu` Image mit `docker run -d`ausführen:
![](image/Pasted%20image%2020250221094206.png)

*Abbildung 5: Ubuntu Image*

Das Image wird heruntergeladen, aber der Container wird nicht gestartet. Das Problem ist, dass das Image kein Programm hat, das ausgeführt wird. 

- `docker run -it`
	- ![](image/Pasted%20image%2020250221094358.png)
	
	 *Abbildung 6: Ubuntu Container im interaktiven Modus*
	- `it` steht für `interactive terminal`.
	- Es wird ein Terminal im Container geöffnet.

- `Interactive Terminal` in einem laufenden `nginx` Container:
  
```bash
docker exec -it nginx /bin/bash
```

![](image/Pasted%20image%2020250221094802.png)


*Abbildung 7: Nginx Container im interaktiven Modus*

![](image/Pasted%20image%2020250221094931.png)

*Abbildung 8: Stoppen des `nginx` Containers*

![](image/Pasted%20image%2020250221095111.png)

*Abbildung 9: Entfernen der Container*

## Registry und Repository

![](image/Pasted%20image%2020250221095655.png)

*Abbildung 10: Private Docker Repository*

## Privates Repository

![](image/Pasted%20image%2020250221100013.png)

*Abbildung 11: Kopieren des `nignx` ins eigene Repository*

![](image/Pasted%20image%2020250221100120.png)

*Abbildung 12: Das Image ins eigene Repository pushen*

- `docker push ezpcy/m347:nginx`:
	- Dieser Befehl lädt das Image in das eigene Repository hoch.

Das gleiche Prozedere für `mariaDB`:

```bash
docker pull mariadb
docker tag mariadb ezpcy/m347:mariadb
docker push ezpcy/m347:mariadb
```

![](image/Pasted%20image%2020250221100446.png)

*Abbildung 13: Das Private Repository mit `nginx` und `mariadb`*
