
# KN06: Kubernetes I

## A) Installation

Drei Instanzen erstellt und auf einem 2 mal  `microk8s add node` ausgeführt und die Instanzen verbunden.

Erlaube Kommunikation auf Ports: 16443,25000,10250,10255,12379,19001,32000/tcp

**`microk8s kubectl get nodes` Ausgabe:**

![](image/Pasted%20image%2020250314093329.png)

_Abbildung1:  Ausgabe von `microk8s kubectl get nodes`_

## B) Verständnis für Cluster

**`microk8s kubectl get nodes` auf der zweiten Instanz:**

![](image/Pasted%20image%2020250314093405.png)

_Abbildung 2: Ausgabe von `microk8s kubectl get nodes` auf der zweiten Instanz_

**`microk8s status` Ausgabe:**

![](image/Pasted%20image%2020250314093501.png)


_Abbildung 3: Ausgabe von `microk8s status`_

**`addons` Definition:**

Rufen Sie den Befehl `microk8s status` auf und schauen Sie die ersten paar Zeilen an (vor "addons"). Was bedeuten diese. Sie finden mehr Information in der Installationsanleitung des Herstellers der Sie gefolgt sind im Kapitel _High Availability_. Erstellen Sie einen Screenshot und einen Erklärungstext

![](image/Pasted%20image%2020250314093932.png)

_Abbildung 4: High Availability aus der Installationsanleitung_

- Wenn Ihr Cluster aus drei oder mehr Knoten besteht, wird der Datenbank über die Knoten repliziert und ist gegen einen einzelnen Ausfall resistent (wenn ein Knoten ein Problem entwickelt, werden Workloads ohne Unterbrechung fortgesetzt).
- Das heisst du hast Redundanz und kannst einen Ausfall verkraften.

**`microk8s leave` aus einem Cluster austreten:**

 ![](image/Pasted%20image%2020250314094957.png)

_Abbildung 5: Ausgabe von `microk8s leave`_

**Node entfernen mit `microk8s remove-node`:**

![](image/Pasted%20image%2020250314095054.png)

_Abbildung6: Ausgabe von `microk8s remove-node`_

**Join als Worker Node:**

![](image/Pasted%20image%2020250314095217.png)

_Abbildung7: Ausgabe von `microk8s join`_

**Erneute Status Ausgabe:**

![](image/Pasted%20image%2020250314095545.png)

_Abbildung8: Ausgabe von `microk8s status`_

**Erklärung**:
- Sobald du einen Node **als Worker** hinzufügst (`microk8s join --worker`), verliert der Cluster die **High Availability (HA)**-Funktionalität, weil **nur der Master-Node (datastore master) die etcd-Datenbank verwalt**
- Ein **Worker-Node (`--worker`) übernimmt keine Steuerungsaufgaben**, daher verliert der Cluster HA.
- Um **HA zurückzubekommen**, müssen **mindestens drei Nodes als Control Plane Nodes** vorhanden sein.

**Nodes auf dem Master:**

![](image/Pasted%20image%2020250314101928.png)

_Abbildung9: Ausgabe von `microk8s kubectl get nodes` auf der Master Node_

Nodes auf dem Worker:

![](image/Pasted%20image%2020250314102007.png)

_Abbildung10: Ausgabe von `microk8s kubectl get nodes` auf der Worker Node_

## **Warum stimmen die Resultate von `kubectl get nodes` und `microk8s status` überein?**

- **`microk8s kubectl get nodes`** zeigt eine **Liste aller Nodes** im Kubernetes-Cluster.
- **`microk8s status`** zeigt den aktuellen Zustand von MicroK8s, einschließlich **welche Nodes Teil des Clusters sind**.
- **Da beide Befehle auf die gleiche Cluster-Datenbank zugreifen, stimmen ihre Ergebnisse überein.**
- Unterschied: `microk8s status` zeigt zusätzliche **Cluster-Informationen** wie **HA-Status, laufende Add-ons und den Datastore-Master**.

## **Erkläre den Unterschied zwischen `microk8s` und `microk8s kubectl` mit eigenen Worten**

| Befehl                 | Bedeutung                                                                                                  |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| **`microk8s`**         | Verwaltung des MicroK8s-Clusters (Starten, Stoppen, Add-ons, Nodes verwalten).                             |
| **`microk8s kubectl`** | Ein in MicroK8s eingebettetes `kubectl`, um Kubernetes-Ressourcen zu verwalten (Pods, Nodes, Deployments). |

- `microk8s` ist das **Hauptverwaltungswerkzeug** für den Cluster, mit dem man ihn starten, stoppen und konfigurieren kann.
- `microk8s kubectl` ist ein in MicroK8s eingebautes Kubernetes-CLI-Tool, das verwendet wird, um **Cluster-Ressourcen zu verwalten** (z. B. Nodes, Pods, Services).