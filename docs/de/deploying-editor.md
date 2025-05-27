---
outline: deep
---

# Bereitstellung des Metadaten-Editors

Wie für den Datahub werden wir nun einen Abschnitt zur `docker-compose.yml` Datei hinzufügen, um die Metadaten-Editor-Anwendung von GeoNetwork-UI ausprobieren zu können.

### 1. Öffnen Sie die `docker-compose.yml` Datei und fügen Sie das Metadata-Editor-Image hinzu

Fügen Sie die folgenden Zeilen zu der `docker-compose.yml` Datei hinzu, die wir zuvor erstellt haben:

```yaml
  metadata-editor:
    image: geonetwork/geonetwork-ui-metadata-editor:2.4.4
    depends_on:
      geonetwork:
        condition: service_healthy
    volumes:
      - ./configuration/:/usr/share/nginx/html/metadata-editor/assets/configuration
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.metadataeditor.rule=Host(`localhost`) && PathPrefix(`/metadata-editor`)"
      - "traefik.http.routers.metadataeditor.entrypoints=web"
```

### 2. Starten Sie den Metadaten-Editor-Container

**Beenden Sie alle laufenden Befehle mit STRG+C.**

Führen Sie den folgenden Befehl in einem Terminal innerhalb des Workshop-Ordners aus:

```shell
docker compose up -d
```

Die Metadaten-Editor-Anwendung sollte unter http://localhost:8080/metadata-editor/ zugänglich sein

![Editor-Oberfläche](../assets/editor-interface.png)

### 3. Erstellen Sie einen neuen Datensatz

Klicken Sie auf "Neuer Datensatz". Dies führt Sie zu einem leeren Formular. Nehmen Sie sich Zeit, die verfügbaren Felder zu überprüfen und füllen Sie diejenigen aus, die Sie möchten.

![Editor-Formular](../assets/editor-form.png)

Beachten Sie, dass die Schlüsselwörter, die wir zuvor erstellt haben, im Abschnitt "Datensatzbeschreibung" verfügbar sein sollten.

![Schlüsselwörter](../assets/keywords.png)

Sie die Seite aktualisieren können, ohne Ihre Arbeit zu verlieren.

Sobald Sie fertig sind, **klicken Sie auf "Veröffentlichen" (Wolken-Symbol) oben rechts.**

Sie können Ihre ausstehenden Änderungen jederzeit rückgängig machen, anstatt sie zu veröffentlichen, indem Sie auf das Symbol "Zurücksetzen" in der oberen linken Ecke klicken.

![Veröffentlichen und zurücksetzen](../assets/publish-revert.png)

### 4. Fügen Sie dem Datensatz eine Datendatei hinzu

Gehen Sie im selben Datensatz zum Tab "Ressourcen".

Laden Sie die Datei hier herunter: <a target="_blank" href="/gs-workshop-geonetwork/fahrradabstellanlagen.geojson">fahrradabstellanlagen.geojson</a>

Schauen Sie sich den Block "Zugehörige Ressourcen" an und wählen Sie "Mit einer Datei verknüpfen".

![Zugehörige Ressourcen](../assets/associated-resources.png)

Hängen Sie die Datei an den Datensatz an, indem Sie sie auf den Bereich "Datei auswählen" ziehen.

### 5. Fügen Sie Links zu Webdiensten hinzu

Wechseln Sie nun zu "Mit einem Dienst verknüpfen". Versuchen Sie, diese beiden Dienste zu verknüpfen:

* URL: https://geoweb1.digistadtdo.de/doris_gdi/geoserver/ALKIS_ADV/ows  
  Protokoll: WMS
* URL: https://geo.kreis-viersen.de/ows/osm-daten  
  Protokoll: WFS

Wählen Sie eine der Ebenen aus jedem dieser Dienste aus. Sie können auch gerne andere Dienste ausprobieren! Es werden viele Protokolle unterstützt.

![Dienste verknüpfen](../assets/linking-services.png)

### 6. Veröffentlichen Sie den Datensatz

Die Schaltfläche "Veröffentlichen" befindet sich oben rechts.

### 7. Öffnen Sie den Datensatz im Datahub

Gehen Sie zu http://localhost:8080/datahub/news.

Sie sollten den geänderten Datensatz oben im Datahub-Newsfeed finden.

![Newsfeed](../assets/datahub-newsfeed.png)

Öffnen Sie den Datensatz: Die Daten sollten jetzt die Karten-, Tabellen- und Diagramm-Vorschauen anzeigen!

![Datenvorschau](../assets/data-preview.png)

![Diagramm-Vorschau](../assets/chart-preview.png)
