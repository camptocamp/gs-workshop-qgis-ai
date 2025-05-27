---
outline: deep
---

# Overview

**GeoNetwork** is an INSPIRE-compliant Geospatial Metadata Catalog.

## Versions

The latest version of GeoNetwork at time of writing is `4.4.6`. The `4.4.x` is a stable branch receiving all new features and bugfixes.

The `4.2.x` branch receives bugfixes and small quality-of-life improvements.

**Other branches (`4.0.x`, `3.x`...) are no longer maintained.**

All versions of GeoNetwork are available on SourceForge: https://sourceforge.net/projects/geonetwork/files/GeoNetwork_opensource/

## Requirements

GeoNetwork relies on the following externals:

* A database
  * GeoNetwork stores many things in the database: metadata records, application settings, groups and users, harvesters,
    privileges, validation runs, etc.
  * by default GeoNetwork uses an H2 embedded database for simplicity (not suited for production)
  * in production PostgreSQL is often used but GeoNetwork also supports Oracle, MySQL and SQL Server
  * supports JNDI connection
* An ElasticSearch cluster
  * Elasticsearch is the workhorse of GeoNetwork's search engine
  * Metadata records are stored in the database and indexed regularly and automatically in ElasticSearch

System requirements are:
* Operating system: Linux, Windows, Mac OS X
* Memory: from 8GB for small catalogs (~2.000 records) to 32GB for large ones (50.000+ records)
* CPU: 2 to 4 cores

## Schema plugins

GeoNetwork can work with any metadata schema through the use of plugins. By default, the following plugins are included:

* Dublin Core
* ISO 19139 (along with ISO 19110)
* ISO 19115-3

Schema plugins are found in the `schemas` folder.

## Back-end

Most backend functions of GeoNetwork now rely on Spring Framework and projects that revolve around it (Spring-security, JPA / Hibernate ...).

Some remaining services still rely on Jeeves and are pending migration to Spring.

## Front-end

The built-in front-end of GeoNetwork is built using AngularJS. Various efforts have arisen in the past few years to modernize this front-end, one of them being the [GeoNetwork-UI project](https://github.com/geonetwork/geonetwork-ui) which now has its own community and roadmap.

You will have the chance to deploy GeoNetwork-UI apps later on in this workshop!
