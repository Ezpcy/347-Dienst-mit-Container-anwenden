# KN07: Kubernetes II

## A) Begriffe und Konzepte erlernen

### *Pods* und *Replicas*

**Pods:**
- Pods sind die kleinste Einheiten von Kubernetes, es ist eine Abstraktion von einem Container.
- Es erstellt einen Layer über einen Container und kann somit einfach wiedererstellt werden.
- Normalerweise befindet sich in einem Pod eine Applikation, welche auch eine Datenbank, Cache oder andere Services enthalten kann.
- Jeder Pod erhält eine eigene IP-Adresse, welche von anderen Pods erreicht werden kann.
- Pods sind ephemeral, was bedeutet, dass sie jederzeit erstellt und zerstört werden können.
**Replicas:**
- Eine Replica ist eine Kopie eines Pods. Ein Deployment oder ReplicaSet sorgt dafür, dass immer eine bestimmte Anzahl von Replikaten (Pods) läuft.

**Zusammenfassung:**
- **Ein Pod ist eine einzelne Einheit**, die eine Anwendung oder einen Dienst ausführt.
- **Eine Replica ist eine identische Kopie eines Pods**, um Skalierbarkeit und Hochverfügbarkeit zu gewährleisten.
- Beispiel: Ein **Webserver-Pod** kann mehrere Replicas haben, um **Lastverteilung und Ausfallsicherheit** sicherzustellen.

### *Service* und *Deployment*

**Service:**
- Ein Service ist ein statische IP-Adresse oder ein permanenter Endpunkt, der an jeden Pod angehängt werden kann. Der Lebenszyklus eines Service ist unabhängig vom Pod.
- Um eine Applikation von außen erreichbar zu machen, muss ein externer Service erstellt werden. Für Datenbanken, die normalerweise nicht von außen erreichbar sein sollten, kann ein interner Service erstellt werden.
- Beispiel:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-service
  spec:
    selector:
      app: mongo
    ports:
      - protocol: TCP
        port: 27017
        targetPort: 27017
```
- 
**Deployment:**
- Ein Deployment ist eine höhere Abstraktion eines Pods, die den Lebenszyklus des Pods verwaltet. Sie können definieren, wie viele Replikate eines Pods Sie ausführen möchten, und wenn ein Pod zerstört wird, wird er neu erstellt.
- Beispiel:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo-deployment
  labels:
    app: mongo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
        - name: mongodb
          image: mongo:5.0
          ports:
            - containerPort: 27017
```

### Ingress

Ingress ermöglicht den Zugriff auf Dienste in einem Kubernetes-Cluster von aussen. **Kubernetes-Services** haben keine öffentliche URL, ausser mit einem **NodePort** oder **LoadBalancer**. **Ingress** bietet eine einfache Möglichkeit, externe Zugriffe auf Dienste in einem Kubernetes-Cluster zu ermöglichen.

Sie ist eine Art von **Reverse Proxy**-Server, der den eingehenden HTTP- und HTTPS-Verkehr auf Dienste in einem Kubernetes-Cluster verteilt. Ingress kann auch SSL/TLS-Terminierung, Lastenausgleich und mehr bieten.

Beispiel:
- Ohne Ingress:
	- `http://192.168.1.200:30001` -> Backend-Service
	- `http://192.168.1.230::30002` -> Frontend-Service
- Mit Ingress:
  - `http://myapp.com/backend` -> Backend-Service
  - `http://myapp.com/frontend` -> Frontend-Service

### StatefulSet

Ein **StatefulSet** ist eine Kubernetes-Controller-Ressource, die für den Betrieb von **stateful Applikationen** verwendet wird. Es ist eine **Erweiterung von ReplicaSet** und **Deployment**. Im Gegensatz zu Pods in einem Deployment oder ReplicaSet haben Pods in einem StatefulSet eine **feste Identität** und **speichern ihren Zustand**.

Ein Merkmal von StatefulSets ist, dass jeder Pod einen eigenen **PersistentVolumeClaim (PVC)** hat, der an einen **PersistentVolume (PV)** gebunden ist. Dadurch wird sichergestellt, dass die Daten auch nach dem Neustart des Pods erhalten bleiben.

Beispiel:
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
  spec:
    serviceName: "nginx"
    replicas: 3
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx
          volumeMounts:
          - name: www
            mountPath: /usr/share/nginx/html
    volumeClaimTemplates:
    - metadata:
        name: www
      spec:
        accessModes: [ "ReadWriteOnce" ]
        resources:
          requests:
            storage: 1Gi
```

## B) Demo Projekt

### 1. Abweichungen zwischen Begriffsdefinitionen und Umsetzung

In Teil A wurden Begriffe wie StatefulSet und Service erklärt. Bei der Umsetzung im Demo-Projekt wurde ein Deployment verwendet. Das Projekt dient für Demonstrationszwecke. In einer Produktionsumgebung wäre es sinnvoller, ein StatefulSet für die Datenbank zu verwenden, um eine persistente Speicherung über Pod-Neustarts hinweg zu gewährleisten. Aussderdem werden nur Kleinigkeiten gespeichert.

### 2. Erklären Sie die MongoUrl in der ConfigMap.yaml

Die **MongoUrl** ist in der ConfigMap.yaml definiert, um eine zentrale Konfigurationsquelle für die Verbindung zur Datenbank bereitzustellen. Dies erlaubt es, Umgebungsvariablen einfach zu ändern, ohne das gesamte Deployment neu zu definieren. Der Wert der MongoUrl ist korrekt, da er auf den DNS-Namen des MongoDB-Services im Cluster verweist. Kubernetes sorgt dafür, dass interne Dienste sich gegenseitig über ihre Servicenamen finden können.

### 3. Nachweis der Installation der App

Führen Sie folgenden Befehl auf mindestens zwei Nodes aus und erstellen Sie Screenshots der Ausgabe:


```
microk8s kubectl describe service webapp-service
```


![](image/Pasted%20image%2020250314130008.png)

_Abbildung 1: Auf der Master Node ausgeführter Befehl_

![](image/Pasted%20image%2020250314130336.png)

_Abbildung 2: Auf der zweiten Node ausgeführter Befehl_

### 4. Vergleich des zweiten Services

```bash
microk8s kubectl describe service mongo-service
```

![](image/Pasted%20image%2020250314130618.png)

_Abbildung 3: Auf der Master Node ausgeführter Befehl_

![](image/Pasted%20image%2020250314130549.png)

_Abbildung 4: Auf der zweiten Node ausgeführter Befehl_



Führen Sie den Befehl für einen weiteren Service aus und vergleichen Sie die Ausgabe:

```
microk8s kubectl describe service <zweiter-service-name>
```

**Unterschiede:**

- `Type` des Services: 
	- `mongo-service`: ClusterIP
	- `webapp-service`: NodePort
- Die Endpunkte und Ports der Services sind unterschiedlich.

### 5. Zugriff auf die Webseite

Aus irgendeinem Grund ist der Body auf `display: none` gesetzt, was dazu führt, dass die Webseite leer ist.

1. [44.209.106.73:30100](44.209.106.73:30100)

![](image/Pasted%20image%2020250314131933.png)

2. [98.83.5.171:30100](98.83.5.171:30100)

![](image/Pasted%20image%2020250314133701.png)

Ich musste die `replicas`auf 3 erhöhen, um die Webseite mit verschiedenen IPs zu erreichen.

### 6. Verbindung zur MongoDB mit Compass

Wenn der Zugriff mit **MongoDB Compass** fehlschlägt, liegt dies wahrscheinlich daran, dass der Service als **ClusterIP** definiert ist. Ein **ClusterIP**-Service ist nur innerhalb des Kubernetes-Clusters erreichbar. Um den Zugriff von außerhalb zu ermöglichen, könnte man den Service als **NodePort** oder **LoadBalancer** bereitstellen.

Mögliche Änderungen:

- **Änderung des Service-Typs von ClusterIP zu NodePort**:
    

```
kind: Service
apiVersion: v1
metadata:
  name: mongodb-service
spec:
  type: NodePort  # Ändern von ClusterIP zu NodePort
  ports:
    - port: 27017
      targetPort: 27017
      nodePort: 32017  # Einen freien Port zuweisen
```

### 7. Änderung der Service-Definition

#### Schritte:

1. Die Service-Definition öffnen und den `nodePort` auf 32000 ändern.
2. `replicas` auf 3 erhöhen.
3. Anwendung und Service neu bereitstellen:
```bash
microk8s kubectl apply -f service.yaml
microk8s kubectl apply -f deployment.yaml
```
1. Webseite über `32000`:
![](image/Pasted%20image%2020250314134552.png)

_Webseite über `32000`_

5. Screenshots der Ausgabe:
![](image/Pasted%20image%2020250314134231.png)

_Abbildung 5: Ausgabe von `microk8s kubectl get pods`_

**Unterschiede:**
- Die Anzahl der **Replicas** ist nun 3 statt 2, wodurch die Lastverteilung verbessert wird.
- Der Port für den externen Zugriff wurde auf **32000** geändert, sodass die Web-App nun unter `http://<Node-IP>:32000` erreichbar ist.