---
outline: deep
---

# Overview

GeoNetwork-UI is a project born in 2020 out of the need to renovate the built-in GeoNetwork user interface, which is built on outdated technologies.

The project is hosted on GitHub at https://github.com/geonetwork/geonetwork-ui.

It is based on Angular and provides:
* A flexible theming system
* A simple to use configuration file
* Many features available outside of the Angular framework as Web Components
* Compatibility with a wide range of GeoNetwork versions
* An NPM package to benefit from the project's components and services in a third-party app

## Structure

GeoNetwork-UI is structured as a [monorepo](https://en.wikipedia.org/wiki/Monorepo). As such, several applications have been built using it. The applications that have received the most features are:

* **Datahub**  
  The Datahub is a easy-to-use and accessible search interface, perfectly suited for a public-facing website.

* **Metadata Editor**  
  the Metadata Editor provides an alternative to the built-in metadata edition interface of GeoNetwork; it is still undergoing development but is already usable.  

## Distribution

All applications provided by the GeoNetwork-UI project are available as ZIP archive or as Docker images on DockerHub:

* https://hub.docker.com/r/geonetwork/geonetwork-ui-datahub

* https://hub.docker.com/r/geonetwork/geonetwork-ui-metadata-editor

ZIP archives are attached to each release on GitHub: https://github.com/geonetwork/geonetwork-ui/releases

## Documentation

A dedicated documentation website is available here: https://geonetwork.github.io/geonetwork-ui/main/docs/

