---
outline: deep
---

# Deployment des Datahub

In diesem Abschnitt werden wir die bestehende Docker-Zusammenstellung anpassen.

### 1. Öffnen der `docker-compose.yml`-Datei und Hinzufügen des Datahub-Images

Füge die folgenden Zeilen in die zuvor erstellte `docker-compose.yml`-Datei ein:

```yaml
  datahub:
    image: geonetwork/geonetwork-ui-datahub:2.4.4
    depends_on:
      geonetwork:
        condition: service_healthy
    volumes:
      - ./configuration/:/usr/share/nginx/html/datahub/assets/configuration
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.datahub.rule=Host(`localhost`) && PathPrefix(`/datahub`)"
      - "traefik.http.routers.datahub.entrypoints=web"
```

### 2. Kopieren der Konfigurationsdatei

bereitgestellte Konfigurationsdatei hier herunter: <a target="_blank" href="/gs-workshop-geonetwork/default.toml">default.toml</a>. Lege diese Datei unverändert in einem Ordner namens `configuration` im selben Verzeichnis wie die `docker-compose.yml`-Datei ab.

### 3. Starten des Datahub-Containers

**Beenden Sie alle laufenden Befehle mit STRG+C.**

Führe im Terminal innerhalb des Workshop-Ordners folgenden Befehl aus:

```shell
docker compose up -d
```

Die Datahub-Anwendung sollte unter http://localhost:8080/datahub/ erreichbar sein.

### 4. Anpassen der Konfiguration

Öffne die heruntergeladene `default.toml`-Datei im `configuration`-Ordner, die du heruntergeladen hast und die vom Datahub gelesen wird. Darin findest du viele Parameter, die du nach Belieben anpassen kannst!

Eine ausführlichere Anleitung zur Anpassung ist hier verfügbar: https://geonetwork.github.io/geonetwork-ui/main/docs/guide/configure.html

Möglichkeiten zur Konfigurationsanpassung:
* Theming: Farben, Hintergrundbild...
* Ändern der erweiterten Filter
* Erstellen vordefinierter Suchen
* Aktivieren mehrerer Sprachen
* Anpassen von Übersetzungen
* Ändern der Hintergrundebenen der Karte
* usw.

### 5. Authentifizierung aktivieren

Einige Funktionen des Datahub sind nur verfügbar, wenn man in GeoNetwork authentifiziert ist:
* Markieren von Datensätzen als Favoriten
* Hinzufügen von Feedback zu Datensätzen

Um die Anmeldung in GeoNetwork zu ermöglichen, muss zunächst der CSRF-Schutz in GeoNetwork deaktiviert werden.

::: warning
Dies sollte nicht auf einer Produktionsinstanz durchgeführt werden! CSRF-Schutz spielt eine sehr wichtige Rolle beim Schutz der Nutzer.

Bitte beachten Sie diesen Leitfaden zur Handhabung in der Produktionsumgebung: https://geonetwork.github.io/geonetwork-ui/main/docs/guide/deploy.html#authentication
:::

```shell
docker compose exec geonetwork bash -c "sed -i 's#<ref bean=\"csrfFilter\" />##' /opt/geonetwork/WEB-INF/config-security/config-security-core.xml"
```

Anschließend muss GeoNetwork neu gestartet werden:

```shell
docker compose restart geonetwork
```

### 6. Anmelden und einen Datensatz als Favoriten markieren

Rufe die Datahub-Oberfläche unter http://localhost:8080/datahub/ auf.

Bei jedem Datensatz gibt es ein "Stern"-Symbol. Wenn du den Mauszeiger darüber bewegst, wird dir ein Anmeldelink angezeigt. Klicke darauf und gib die Anmeldedaten des zuvor erstellten Benutzers ein.

Nach der Anmeldung wirst du zurück zum Datahub geleitet. Nun kannst du Datensätze als Favoriten markieren, nur deine Favoriten filtern und Datensätze sogar nach der Anzahl der Nutzer sortieren, die diese als Favoriten gesetzt haben!
