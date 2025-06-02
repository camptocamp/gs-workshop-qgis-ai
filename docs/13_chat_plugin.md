---
outline: deep
---

# Chatbot web : Générer un plugin QGIS

Maintenant que le code est fonctionnel, nous allons créer un plugin QGIS qui affiche les bureaux de Camptocamp sur une carte.

_> Très bien, je voudrais maintenant générer un plugin à partir de ce code_

## Exemple de réponse de ChatGPT

### 🧩 Plugin QGIS : "Locaux Camptocamp"
#### 📍 Fonctionnalité
Ce plugin ajoute un bouton dans la barre d’outils de QGIS. Lorsqu'on clique dessus, il ajoute un point (marqueur) sur la carte aux emplacements des bureaux de Camptocamp.

#### 📦 Arborescence du plugin
```bash
camptocamp_locaux/
├── __init__.py
├── camptocamp_locaux.py
├── camptocamp_locaux_dialog.py
├── camptocamp_locaux_dialog_base.ui
├── metadata.txt
├── icon.png
└── resources.qrc
```
#### 📁 metadata.txt
```ini
[general]
name=Camptocamp Locaux
qgisMinimumVersion=3.0
description=Affiche les bureaux de Camptocamp sur la carte
version=1.0
author=Florent Gravin
email=florent.gravin@camptocamp.com
```
#### 🧠 __init__.py
```py
def classFactory(iface):

from .camptocamp_locaux import CamptocampLocaux
return CamptocampLocaux(iface)
```
#### 🧰 camptocamp_locaux.py
```py
from qgis.PyQt.QtWidgets import QAction, QMessageBox
from qgis.core import QgsPointXY, QgsProject, QgsVectorLayer, QgsFeature, QgsGeometry, QgsFields, QgsField
from qgis.PyQt.QtCore import QVariant
from PyQt5.QtGui import QIcon
import os

class CamptocampLocaux:
    def __init__(self, iface):
    self.iface = iface
self.plugin_dir = os.path.dirname(__file__)

def initGui(self):
    icon = QIcon(os.path.join(self.plugin_dir, "icon.png"))
    self.action = QAction(icon, "Afficher les locaux Camptocamp", self.iface.mainWindow())
    self.action.triggered.connect(self.add_locations)
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("Camptocamp Locaux", self.action)

def unload(self):
    self.iface.removePluginMenu("Camptocamp Locaux", self.action)
    self.iface.removeToolBarIcon(self.action)

def add_locations(self):
    layer = QgsVectorLayer("Point?crs=EPSG:4326", "Locaux Camptocamp", "memory")
    pr = layer.dataProvider()
    pr.addAttributes([
        QgsField("Nom", QVariant.String),
        QgsField("Ville", QVariant.String)
    ])
    layer.updateFields()

    locations = [
        ("Camptocamp - France", "Chambéry", QgsPointXY(5.9185, 45.5646)),
        ("Camptocamp - Suisse", "Lausanne", QgsPointXY(6.6323, 46.5197)),
        ("Camptocamp - Allemagne", "Freiburg", QgsPointXY(7.8522, 47.9990))
    ]

    features = []
    for name, city, point in locations:
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPointXY(point))
        feat.setAttributes([name, city])
        features.append(feat)

    pr.addFeatures(features)
    layer.updateExtents()
    QgsProject.instance().addMapLayer(layer)
    QMessageBox.information(self.iface.mainWindow(), "Camptocamp", "Les locaux ont été ajoutés à la carte.")

```
#### 🖼️ icon.png
Placez une icône 32x32 dans le répertoire du plugin pour le bouton dans la barre d’outils.

#### 🚀 Installation
1. Zipper le dossier camptocamp_locaux/
2. Dans QGIS : Extensions > Installer/Gérer les extensions > Installer depuis un ZIP
3. Activez-le dans le gestionnaire.
