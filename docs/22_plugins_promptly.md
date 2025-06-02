---
outline: deep
---

# Promptly

https://github.com/hamarshehmhmd/promptly

:::info
Nous utiliserons le use case "Localisation des stations de métro" pour illustrer l'utilisation de Promptly et comparer avec IntelligGeo.
:::

## Installer le plugin

Ouvrez le panneau des plugins dans QGIS et recherchez "Promptly". Installez le plugin.


## Zoom sur la couche

_zoom sur la couche des stations de métro_

* Promptly ne trouve pas la couche, il faut donner le nom exact de la couche dans le projet QGIS. Par contre, il propose une liste de couche à choisir.
* Promptly zoome sur Null Island, il n'est pas capable de comprendre la projection de la couche. Il faut donc lui indiquer le système de coordonnées de la couche.

_zoom sur la couche mobilite_et_transport_stations_metro, attention, elle est en projection 4326 alors que le projet est en 3857_

```python
from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem, Qgis
from qgis.utils import iface
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QDialog, QComboBox

# Layer name to work with
layer_name = "mobilite_et_transport_stations_metro"

# Find the layer in the current project
selected_layer = None
for lyr in QgsProject.instance().mapLayers().values():
    if lyr.name() == layer_name:
        selected_layer = lyr
        break

if selected_layer:
    # Check the CRS of the layer
    current_crs = selected_layer.crs().authid()
    
    if current_crs == "EPSG:4326":
        # Ensure the project is in EPSG:3857
        project_crs = QgsProject.instance().crs()
        if project_crs.authid() != "EPSG:3857":
            QgsProject.instance().setCrs(QgsCoordinateReferenceSystem("EPSG:3857"))
            iface.messageBar().pushMessage("Info", "Project CRS set to EPSG:3857", level=Qgis.Info)
        
        # Reproject the layer to match the project CRS
        selected_layer.setCrs(QgsCoordinateReferenceSystem("EPSG:3857"), False)
        iface.messageBar().pushMessage("Info", f"Layer '{layer_name}' reprojected to EPSG:3857", level=Qgis.Info)
        
    # Zoom to the layer extent
    extent = selected_layer.extent()
    iface.mapCanvas().setExtent(extent)
    iface.mapCanvas().refresh()
    iface.messageBar().pushMessage("Success", f"Zoomed to layer '{layer_name}'", level=Qgis.Info)
else:
    iface.messageBar().pushMessage("Error", f"Layer '{layer_name}' not found", level=Qgis.Warning)
```

Promptly, comme IntelliGeo, n'a pas accès au contexte du projet QGIS. Il ne dispose pas d'agent, ni de tools utilisables par le LLM. De ce fait, le LLM a du mal à comprendre le contexte et répondre correctement aux questions posées.

Pour plus de précision et d'interaction avec le projet QGIS, il faut s'interfacer avec un serveur MCP.

