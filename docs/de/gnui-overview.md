---
outline: deep
---

# Überblick

GeoNetwork-UI ist ein Projekt, das 2020 aus der Notwendigkeit heraus entstanden ist, die in GeoNetwork integrierte Benutzeroberfläche zu modernisieren, da diese auf veralteten Technologien basiert.

Das Projekt ist auf GitHub gehostet unter: https://github.com/geonetwork/geonetwork-ui.

Es basiert auf Angular und bietet:
* Ein flexibles Themensystem
* Eine einfach zu verwendende Konfigurationsdatei
* Viele Funktionen, die außerhalb des Angular-Frameworks als Web Components verfügbar sind
* Kompatibilität mit einer Vielzahl von GeoNetwork-Versionen
* Ein NPM-Paket, um von den Komponenten und Diensten des Projekts in einer Drittanbieter-App zu profitieren

## Struktur

GeoNetwork-UI ist als [Monorepo](https://de.wikipedia.org/wiki/Monorepo) strukturiert. In diesem Rahmen wurden mehrere Anwendungen entwickelt. Die am meisten erweiterten Anwendungen sind:

* **Datahub**  
  Der Datahub ist eine benutzerfreundliche und barrierefreie Suchoberfläche, die sich perfekt für eine öffentliche Website eignet.

* **Metadaten-Editor**  
  Der Metadaten-Editor bietet eine Alternative zur integrierten Metadaten-Bearbeitungsoberfläche von GeoNetwork. Er befindet sich noch in der Entwicklung, ist aber bereits nutzbar.

## Distribution

Alle Anwendungen des GeoNetwork-UI-Projekts sind als ZIP-Archiv oder als Docker-Images auf DockerHub verfügbar:

* https://hub.docker.com/r/geonetwork/geonetwork-ui-datahub

* https://hub.docker.com/r/geonetwork/geonetwork-ui-metadata-editor

ZIP-Archive sind an jede Veröffentlichung auf GitHub angehängt: https://github.com/geonetwork/geonetwork-ui/releases

## Dokumentation

Eine dedizierte Dokumentationswebsite ist hier verfügbar: https://geonetwork.github.io/geonetwork-ui/main/docs/
