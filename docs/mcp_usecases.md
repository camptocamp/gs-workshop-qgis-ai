---
outline: deep
---

# Introduction

Maintenant que nous avons mis en place un Agent avec le serveur MCP qui communique avec QGIS nous allons tester des scénarios de conversations plus ou moins complexes.

# Uses cases

## Tester le fonctionnement

```text
Quelle est ma version de QGIS ?
```

## Ajouter une couche

```text
Peux-tu ajouter dans QGIS la couche MNT france entière qui se trouve quelque part dans ~/data/IGN ?
```

## Créer un style

```text
Peux-tu me changer le style de la couche département pour afficher les noms de département dans les étiquettes
```

```text
Peux-tu me générer des styles sur toutes mes couches pour obtenir un rendu cohérent et performant à toutes les échelles qui sont pertinentes à la vue des données.

Je voudrais des étiquettes avec les nom des entités territoriales.
```

=> Problème les géométries explosent le contexte, il faudrait pouvoir récupérer uniquement la liste des champs, ou un feature sans geometrie.

## Créer un plugin

```text
Sachant que nous avons ici un plugin minimal pour QGIS : https://github.com/wonder-sk/qgis-minimal-plugin

Je voudrais que tu me créer ici un dossier avec un plugin qui trie les couches, raster en bas, puis polygones, puis lignes et points
```

```text
Je viens de créer qgis_sort_layers_plugin peut tu m'ajouter un makefile pour le charger facilement dans QGIS avec un lien symbolique.
```
