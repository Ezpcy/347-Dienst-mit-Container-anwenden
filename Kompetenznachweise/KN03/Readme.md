# KN03: Netzwerk, Sicherheit

## Container und Netzwerk Erstellung

### Befehle zur Erstellung der Container und des Netzwerks

![](image/Pasted%20image%2020250227131149.png)

_Abbildung 1: Erstellung der Container und des Netzwerks_


### IP-Adressen der Container

![](image/Pasted%20image%2020250227132608.png)

_Abbildung 2: Docker inspect Befehl für IP-Adressen_

### Default Gateway

![](image/Pasted%20image%2020250227132211.png)

_Abbildung 3: Gateway der 4 Container_

`busybox1`und `busybox2` haben den selben Gateway: `172.17.0.1
`busybox2` und `busybox4` haben den selben Gateway: `172.19.0.1


## Ping Befehle

**`busybox1`**:

![](image/Pasted%20image%2020250228071254.png)

_Abbildung 4: Ping Befehle von `busybox1`ausgeführt_

**`busybox3`**:

![](image/Pasted%20image%2020250228071529.png)

_Abbildung 5: Ping Befehle von `busybox3` ausgeführt_

## Fazit

**Gemeinsamkeiten:**
1. **Container-Kommunikation über IP**
2. **Automatische IP-Zuweisung**
3. **Isolation von Containern ausserhalb des Netzwerkes**

**Unterschiede:**
1. **Namensauflösung:**
	- Im **Default-Bridge-Netzwerk** können Container sich nicht über ihre Namen, nur über IP-Adressen.
2. **Netzwerksteuerung:**
	- Das Default-Bridge-Netzwerk ist eine vordefinierte Umgebung mit eingeschränkter Kontrolle.
	- Das erstellte `tbz` Netzwerks bietet mehr Kontrolle über die Netzwerkkonfiguration.
3. **Isolation:**
	- Container in unterschiedlichen Netzwerken können nicht miteinander kommunizieren, man könnte sie jedoch verbinden mit dem Befehl `docker network connect`.
### Bezug zu KN02

Die Container von **KN02** konnten miteinander kommunizieren, weil ihre beiden Netzwerke mit dem Befehl `docker network connect` verbunden wurden.
