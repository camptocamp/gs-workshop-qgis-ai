---
outline: deep
---

# Chatbot web : use case Camptocamp

L'objectif ici est de créer un plugin QGIS qui affiche les bureaux de Camptocamp sur une carte. Nous allons utiliser un chatbot pour générer le code nécessaire à la création de ce plugin.

:::info
Nous pardons du postulat que vous avez déjà installé QGIS et que vous êtes familier avec son interface. Cependant, l'assistant doit vous guider à travers les étapes de création du plugin, même si vous n'avez pas d'expérience préalable en développement de plugins QGIS.
:::

:::info
Nous utiliserons des LLMs tels que Mistral ou ChatGPT pour générer le code Python nécessaire à la création du plugin QGIS.
:::

## Étape 1 : Introduire le contexte

Demandez au chatbot directement ce que vous voulez faire. Par exemple, vous pouvez dire :

_Je veux créer un plugin QGIS qui affiche les bureaux de Camptocamp sur une carte._

Cela permet de voir au premier abord ce que le chatbot comprend et ce qu'il est capable de générer.

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

