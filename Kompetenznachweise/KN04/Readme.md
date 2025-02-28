# KN04: Docker Compose

## Docker Compose: Lokal

### a)

**Befehl**:

![](image/Pasted%20image%2020250228091917.png)

_Abbildung 1: Compose Befehl zur Erstellung der Container_

1. Der Webserver wird über ein **Dockerfile** gebaut.
2. Image Metadaten werden geleden.
3. `.dockerignore` wird versucht zu lesen.
4. Basis Image wird heruntergeladen.
5. Vordefinierte Schritte aus dem **Dockerfile** werden ausgeführt.
6. Fertiges Image wird exportiert.
7. **Netzwerk** wird erstellt.
8. Datenbank container wird erstellt.
9. Beide Container werden gestartet.

`docker compose` führt folgende Befehle aus:

- `docker pull` - Lädt das Image herunter
- `docker create` - Erstellt den Container
- `docker start` - Startet den Container

Mit der `--build` Option wird das Image neu erstellt.

## `info.php`

![](image/Pasted%20image%2020250228092124.png)

_Abbildung 2: `REMOTE_ADDR` und `SERVER_ADDR` aus `info.php`_

`db.php`:

![](image/Pasted%20image%2020250228092326.png)

_Abbildung 3: `db.php`_

### b)

[docker-compose.yml](b/docker-compose.yml)

`info.php`:

![](image/Pasted%20image%2020250228101240.png)

_Abbildung 4: `info.php` von Aufgabe b_

`db.php`:

![](image/Pasted%20image%2020250228095929.png)

_Abbildung 5: `db.php` von Aufgabe b_

**Wieso tritt dieser Fehler auf?**

Der Fehler tritt auf weil der Container die angegebene aus dem **Dockerfile** von dem eigentlichen Container Namen abweicht. Um das Problem zu lösen, müsste der **Servername** angepasst werden.

## Docker Compose: Cloud

`info.php`:

![](image/Pasted%20image%2020250228110554.png)

_Abbildung 6: `info.php` von der AWS Instanz_

`db.php`:

![](image/Pasted%20image%2020250228110655.png)

_Abbildung 7: `db.php` von der AWS Instanz_

![`cloud-init` Datei](cloud-init.yml)