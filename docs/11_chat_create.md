---
outline: deep
---

# Chatbot : générer de scripts python pour QGIS

:::info
Nous utiliserons des LLMs tels que Mistral ou ChatGPT pour générer le code Python nécessaire à la création du plugin QGIS.
:::

## Étape 1 : Introduire le contexte

Demandez au chatbot directement ce que vous voulez faire :

_Je suis un utilisateur de QGIS et je sais coder quelques scripts python.
Je voudrais créer un script qui m'affiche les bureaux de camptocamp.com sur une carte (un fond de plan OSM par exemple)_

## Tester le code généré

Ouvrir la console python de QGIS (Ctrl+Alt+P) et coller le code généré par le chatbot.


```python
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
import requests

# Étape 1 : adresses des bureaux Camptocamp
bureaux = {
    "Le Bourget-du-Lac, France": "Le Bourget-du-Lac, France",
    "Chambéry, France": "Chambéry, France",
    "Lausanne, Suisse": "Lausanne, Switzerland",
    "Olten, Suisse": "Olten, Switzerland",
    "Basel, Suisse": "Basel, Switzerland",
    "Munich, Allemagne": "Munich, Germany"
}

# Étape 2 : géocodage avec Nominatim (OpenStreetMap)
def geocode(adresse):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': adresse,
        'format': 'json',
        'limit': 1
    }
    r = requests.get(url, params=params, headers={'User-Agent': 'QGIS Script'})
    if r.ok and r.json():
        coord = r.json()[0]
        return float(coord['lon']), float(coord['lat'])
    return None

# Étape 3 : création d'une couche mémoire
layer = QgsVectorLayer("Point?crs=EPSG:4326", "Bureaux Camptocamp", "memory")
pr = layer.dataProvider()
pr.addAttributes([QgsField("Nom", QVariant.String)])
layer.updateFields()

# Ajout des points
for nom, adresse in bureaux.items():
    coord = geocode(adresse)
    if coord:
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(coord[0], coord[1])))
        fet.setAttributes([nom])
        pr.addFeature(fet)

layer.updateExtents()
QgsProject.instance().addMapLayer(layer)

# Étape 4 : ajouter le fond OSM si non déjà présent
osm_url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"
osm_layer = QgsRasterLayer(osm_url, "OSM", "wms")
QgsProject.instance().addMapLayer(osm_layer)

# Étape 5 : centrer sur les points
iface.mapCanvas().setExtent(layer.extent())
iface.mapCanvas().refresh()
```

Le code ne s'exécute pas ? Pas de panique, il y a sûrement une erreur dans le code généré. Vous pouvez demander au chatbot de corriger le code en lui fournissant le message d'erreur.

```python
Canevas Traceback (most recent call last):
  File "/usr/lib/python3.10/code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 73, in _maybe_compile
    return compiler(source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
  File "<input>", line 1
    from qgis.core import *

```

Mettez à jour le code en fonction des retours du chatbot, et testez à nouveau.

```python
from qgis.core import *
from qgis.utils import iface
from PyQt5.QtCore import QVariant
```

De cette manière, vous devriez être capable de corriger les erreurs et d'exécuter le code généré par le chatbot.