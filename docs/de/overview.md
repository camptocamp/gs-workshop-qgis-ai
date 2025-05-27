---
outline: deep
---

# Überblick

**GeoNetwork** ist ein INSPIRE-konformes Geospatial-Metadatenkatalogsystem.

## Versionen

Die neueste Version von GeoNetwork zum Zeitpunkt der Erstellung dieses Dokuments ist `4.4.6`. Der `4.4.x`-Branch ist eine stabile Version, die alle neuen Funktionen und Fehlerkorrekturen erhält.

Der `4.2.x`-Branch enthält Fehlerkorrekturen und kleinere Verbesserungen der Benutzerfreundlichkeit.

**Andere Versionen (`4.0.x`, `3.x`...) werden nicht mehr gewartet.**

Alle Versionen von GeoNetwork sind auf SourceForge verfügbar: https://sourceforge.net/projects/geonetwork/files/GeoNetwork_opensource/

## Anforderungen

GeoNetwork ist auf folgende externe Komponenten angewiesen:

* Eine Datenbank
  * GeoNetwork speichert viele Elemente in der Datenbank: Metadatensätze, Anwendungseinstellungen, Gruppen und Benutzer, Harvesting-Dienste,
    Berechtigungen, Validierungsläufe usw.
  * Standardmäßig verwendet GeoNetwork eine eingebettete H2-Datenbank zur Vereinfachung (nicht für den Produktivbetrieb geeignet)
  * Im Produktivbetrieb wird oft PostgreSQL verwendet, aber GeoNetwork unterstützt auch Oracle, MySQL und SQL Server
  * Unterstützt JNDI-Verbindungen
* Ein ElasticSearch-Cluster
  * Elasticsearch ist das Herzstück der Suchmaschine von GeoNetwork
  * Metadatensätze werden in der Datenbank gespeichert und regelmäßig sowie automatisch in ElasticSearch indexiert

Systemanforderungen:
* Betriebssystem: Linux, Windows, Mac OS X
* Arbeitsspeicher: ab 8 GB für kleine Kataloge (~2.000 Datensätze) bis zu 32 GB für große Kataloge (50.000+ Datensätze)
* CPU: 2 bis 4 Kerne

## Schema-Plugins

GeoNetwork kann mit beliebigen Metadatenschemata durch die Nutzung von Plugins arbeiten. Standardmäßig sind folgende Plugins enthalten:

* Dublin Core
* ISO 19139 (zusammen mit ISO 19110)
* ISO 19115-3

Schema-Plugins befinden sich im Ordner `schemas`.

## Back-End

Die meisten Back-End-Funktionen von GeoNetwork basieren inzwischen auf dem Spring Framework und zugehörigen Projekten (Spring Security, JPA / Hibernate usw.).

Einige verbleibende Dienste basieren noch auf Jeeves und stehen zur Migration auf Spring an.

## Front-End

Das integrierte Front-End von GeoNetwork basiert auf AngularJS. In den letzten Jahren gab es verschiedene Bemühungen, dieses Frontend zu modernisieren, darunter das [GeoNetwork-UI-Projekt](https://github.com/geonetwork/geonetwork-ui), das mittlerweile eine eigene Community und Roadmap hat.

Später im Workshop haben Sie die Gelegenheit, GeoNetwork-UI-Anwendungen bereitzustellen!
