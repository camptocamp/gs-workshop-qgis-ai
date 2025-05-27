# Deployment

GeoNetwork ist eine Java-Webanwendung. Es wird als WAR-Datei verteilt, die in einem Java-Servlet-Container (z.B. Apache Tomcat oder Jetty) bereitgestellt werden kann.

Dieser Abschnitt beschreibt zwei Möglichkeiten, GeoNetwork zu deployen: mit **Docker** und **Docker-Compose** sowie mit einer **lokalen Installation**.

## Verwendung von Docker und Docker-Compose

Jede Version von GeoNetwork wird auch als Docker-Image mit einer leichten Verzögerung verteilt. Docker-Images sind auf DockerHub unter
https://hub.docker.com/_/geonetwork zu finden.

Die entsprechenden Dockerfiles finden sich unter https://github.com/geonetwork/docker-geonetwork. Dieses Repository enthält auch Docker-Compose-Dateien, um GeoNetwork einfach mit einer PostgreSQL-Datenbank und einem ElasticSearch-Cluster zu deployen.

### 1. Erstellen Sie einen eigenen Ordner

Klicken Sie mit der rechten Maustaste auf den Desktop-Hintergrund und erstellen Sie einen Ordner mit dem Namen "GeoNetwork Workshop".

![Ordner erstellen](../assets/create-folder.png)

### 2. Erstellen Sie eine `docker-compose.yml` Datei in diesem Ordner

Laden Sie die [docker-compose.yml](/docker-compose.yml) Datei für diesen Workshop herunter oder kopieren Sie deren Inhalt und legen Sie sie in den neu erstellten Ordner.

### 3. Starten Sie den `geonetwork` Service

Öffnen Sie den "GeoNetwork Workshop" Ordner und klicken Sie mit der rechten Maustaste darauf, um ein Terminal zu öffnen:

![Terminal öffnen](../assets/open-terminal.png)

Dieses Terminal wird während des gesamten Workshops verwendet. Führen Sie nun die folgenden Befehle aus:

```shell
docker compose up -d
docker compose logs -f geonetwork
```

Nach einer Weile sollten Sie die folgende Zeile im GeoNetwork-Ausgabeprotokoll sehen:

![Startup message](../assets/gn-startup.png)

Herzlichen Glückwunsch! GeoNetwork läuft jetzt auf Ihrem Computer. Öffnen Sie http://localhost:8080/geonetwork/, um zu bestätigen, dass die Instanz auf Webanfragen reagiert.

![Empty GeoNetwork](../assets/gn-empty.png)

Keine Sorge wegen des Fehlers; die Datenbank ist komplett leer, sodass die Suchanfragen nicht erfolgreich sein werden. Dies wird verschwinden, sobald wir einige Datensätze hinzugefügt haben.

## Verwendung des WAR-Pakets (optional)

Diese Methode erfordert die Installation der folgenden Komponenten auf Ihrem Computer:
* Java 11 oder höher (OpenJDK wird empfohlen)
* Apache Tomcat oder Jetty (Version 9 wird empfohlen)

Für diese Methode werden wir keine PostgreSQL-Datenbank konfigurieren. Stattdessen lassen wir GeoNetwork seine eigene lokale **h2**-Datenbank erstellen; bitte beachten Sie, dass dieser Datenbanktyp nicht für den Produktionseinsatz geeignet ist!

### 1. Laden Sie die WAR-Datei herunter

Öffnen Sie ein Terminal in Ihrem Home-Verzeichnis und führen Sie den folgenden Befehl aus:

```shell
wget https://downloads.sourceforge.net/project/geonetwork/GeoNetwork_opensource/v4.4.6/geonetwork.war
```

### 2. Kopieren Sie die WAR-Datei in den Java-Webserver

Führen Sie den folgenden Befehl in Ihrem Terminal aus:

```shell
cp geonetwork.war /usr/share/apache-tomcat{X}/webapps/.
```

:::: info
Beachten Sie, dass der Pfad, in den die WAR-Datei kopiert werden muss, vom verwendeten Servlet-Container abhängt. Das obige Beispiel gilt für eine Standardinstallation von Apache Tomcat.
::::

### 3. Starten Sie den Java-Webserver

Wenn gestartet, wird Tomcat/Jetty die Anwendung automatisch bereitstellen. Wenn nicht, starten Sie den Java-Webserver, um die Bereitstellung durchzuführen. Bitte beziehen Sie sich auf die Dokumentation des von Ihnen verwendeten Servlet-Containers für diesen Schritt.

Öffnen Sie http://localhost:8080/geonetwork/, um zu bestätigen, dass die Instanz auf Webanfragen reagiert.
