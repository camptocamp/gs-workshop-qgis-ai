---
outline: deep
---

# Chatbot web : itérer

Une fois le script testé et fonctionnel, nous allons demander quelques modifications : 
- utiliser une **icone pour représenter les bureaux de Camptocamp** sur la carte.

:::tip
Utilisez la fonctionnalité **Canvas** de votre Chatbot, cela lui permet de modifier à la volée le code généré.
:::


## Demander des modifications

_Je voudrais mettre une icone pour les bureaux, au lieu des points.
Je l'ai téléchargée, elle s'appelle favicon.png._

**Voici la réponse du chatbot :**

**📁 1. Assure-toi que :**
favicon.png est accessible localement (ex. : /home/ton_nom/favicon.png)

Le chemin est absolu (pas relatif)

**🧑‍💻 2. Ajoute ce code après l’ajout de la couche dans le projet**

```python
icon_path = "/chemin/vers/favicon.png"  # <-- à adapter !

# Crée un symbole basé sur l'image
symbol = QgsMarkerSymbol.createSimple({
    'name': 'image',
    'image': icon_path,
    'size': '10'  # taille de l’icône en mm
})

# Appliquer le symbole à la couche
vl.renderer().setSymbol(symbol)
vl.triggerRepaint()

```
Cela permet de voir au premier abord ce que le chatbot comprend et ce qu'il est capable de générer.

## Tester et corriger

Malheureusement, le code généré ne fonctionne pas tel quel. 

_> l'icone ne s'affiche pas_

**✅ Solution fonctionnelle : utiliser QgsRasterMarkerSymbolLayer**

Voici le code corrigé à insérer pour que ton favicon.png s’affiche :

```python
from qgis.core import QgsRasterMarkerSymbolLayer, QgsMarkerSymbol

# Appliquer une icône PNG avec RasterMarkerSymbolLayer
symbol_layer = QgsRasterMarkerSymbolLayer(icon_path)
symbol_layer.setSize(10)  # en mm

# Créer un symbole vide et y ajouter la couche raster
symbol = QgsMarkerSymbol()
symbol.changeSymbolLayer(0, symbol_layer)

# Appliquer à la couche
vl.renderer().setSymbol(symbol)
vl.triggerRepaint()
```

## Résultat final
Le script complet qui fonctionne !

```python
from qgis.core import *
from qgis.utils import iface
from PyQt5.QtCore import QVariant
from qgis.core import QgsRasterMarkerSymbolLayer, QgsMarkerSymbol

import requests

# Dictionnaire des bureaux
bureaux = {
    "Le Bourget-du-Lac": "Le Bourget-du-Lac, France",
    "Chambéry": "Chambéry, France",
    "Lausanne": "Lausanne, Switzerland",
    "Olten": "Olten, Switzerland",
    "Basel": "Basel, Switzerland",
    "Munich": "Munich, Germany"
}

# Fonction de géocodage avec Nominatim
def geocode(adresse):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': adresse,
        'format': 'json',
        'limit': 1
    }
    try:
        r = requests.get(url, params=params, headers={'User-Agent': 'QGIS Script'})
        r.raise_for_status()
        results = r.json()
        if results:
            lon = float(results[0]['lon'])
            lat = float(results[0]['lat'])
            return lon, lat
    except Exception as e:
        print(f"Erreur pour {adresse} : {e}")
    return None

# Créer une couche mémoire
vl = QgsVectorLayer("Point?crs=EPSG:4326", "Bureaux Camptocamp", "memory")
pr = vl.dataProvider()
pr.addAttributes([QgsField("Nom", QVariant.String)])
vl.updateFields()

# Ajouter les points des bureaux
for nom, adresse in bureaux.items():
    coords = geocode(adresse)
    if coords:
        feat = QgsFeature()
        point = QgsPointXY(coords[0], coords[1])
        feat.setGeometry(QgsGeometry.fromPointXY(point))
        feat.setAttributes([nom])
        pr.addFeature(feat)

vl.updateExtents()
QgsProject.instance().addMapLayer(vl)

# Appliquer une icône personnalisée
icon_path = "/votre-chemin/public/favicon.png"  # Remplace par ton chemin local

symbol_layer = QgsRasterMarkerSymbolLayer(icon_path)
symbol_layer.setSize(10)  # en mm

# Créer un symbole vide et y ajouter la couche raster
symbol = QgsMarkerSymbol()
symbol.changeSymbolLayer(0, symbol_layer)

vl.renderer().setSymbol(symbol)

# Activer l'infobulle au survol
vl.setDisplayExpression('"Nom"')
vl.setMapTipTemplate('<b>Bureau :</b> [% "Nom" %]')
vl.triggerRepaint()

# Ajouter fond OSM si absent
tile_url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
osm_exists = any(layer.name() == "OSM" for layer in QgsProject.instance().mapLayers().values())
if not osm_exists:
    osm_layer = QgsRasterLayer(tile_url, "OSM", "wms")
    if osm_layer.isValid():
        QgsProject.instance().addMapLayer(osm_layer)
    else:
        print("Erreur : couche OSM invalide")

# Zoom sur les bureaux
iface.mapCanvas().setExtent(vl.extent())
iface.mapCanvas().refresh()

```