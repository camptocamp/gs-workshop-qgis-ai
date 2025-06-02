---
outline: deep
---

# Intelligeo

Intelligeo est un plugin QGIS qui permet d'utiliser des modèles de langage (LLM) pour générer du code Python, des requêtes SQL, et d'autres tâches liées à la géomatique. Il est conçu pour faciliter l'interaction avec les LLM et améliorer la productivité des utilisateurs de QGIS.

Decouvrez la section Tutorials de [IntelliGeo](https://www.intelligeo.org/tutorials) pour en savoir plus.

:::info
Nous utiliserons le use case "Localisation des stations de métro" pour illustrer l'utilisation d'IntelliGeo.
:::

## Installer le plugin

Ouvrez le panneau des plugins dans QGIS et recherchez "IntelliGeo". Installez le plugin. Il faut activer les **plugins expérimentaux** dans les paramètres de QGIS pour pouvoir l'installer.

Voir [la documentation officielle](https://www.intelligeo.org/docs/installation) pour plus de détails.

## Télécharger les données

_Je voudrais charger un jeu de données sur les Localisation des stations de métro
à Lille_

```
IntelliGeo 06 02 2025 13:45:58

Pour charger un jeu de données sur QGIS, suivez ces étapes : 

1. Cliquez sur "Layer" dans la barre de menu, puis sélectionnez "Add Layer" 
et choisissez le type de couche approprié (par exemple, "Add Vector Layer" 
pour un fichier .shp, "Add Raster Layer" pour un fichier .tif, etc.). 

2. Dans la fenêtre qui s'ouvre, cliquez sur "Browse" pour naviguer jusqu'à 
l'emplacement de votre jeu de données. 3. Sélectionnez le fichier de données que 
vous souhaitez charger et cliquez sur "Open". Le jeu de données sera alors chargé 
dans votre projet QGIS. Si votre jeu de données est stocké en ligne, vous pouvez 
utiliser l'option "Add WMS/WMTS Layer" ou "Add XYZ Layer" pour charger les données 
à partir d'une URL. Notez que si votre jeu de données est dans un format non 
standard pour QGIS, vous devrez peut-être utiliser un plugin ou un outil de 
conversion pour le rendre compatible._
```

:::warning
IntelliGeo ne recherche pas sur le web, et n'est pas capable de trouver des jeux de données en ligne. Il est conçu pour lire la documentation de QGIS et générer du code Python pour des tâches spécifiques.
:::

Téléchargez le jeu de données sur [la plateforme de la MEL](https://data.lillemetropole.fr/catalogue/dataset/41b39a88-214f-4965-a1d3-6d6ccebc44cc) et ajoutez-le à votre projet QGIS.

### Interroger IntelliGeo pour anayser les données

:::warning
Vous devez explicitement demander à IntelliGeo de générer un script pour votre demande, sinon il recherche dans la documentation et répond du texte.
:::

_génère un script qui compte le nombre de lignes de métro dans la couche mobilite_et_transport_stations_metro_

```python
# Import the necessary QGIS modules
from qgis.core import QgsProject

# Get the current QGIS project instance
project = QgsProject.instance()

# Get the layer by its name
layer = project.mapLayersByName('mobilite_et_transport_stations_metro')[0]

# Initialize a counter for the metro lines
metro_line_count = 0

# Iterate over each feature (i.e., metro station) in the layer
for feature in layer.getFeatures():
    # Get the value of the 'line' attribute, which represents the metro line
    line = feature['line']
    
    # If the line is not None or empty, increment the counter
    if line is not None and line.strip() != '':
        metro_line_count += 1

# Print the total number of metro lines
print('Total number of metro lines:', metro_line_count)
```

:::danger
Il ne comprend pas la structure du jeu de données, et compte les features au lieu de compter les lignes de métro.
:::

ChatGPT lui analyse la structure du jeu de données et génère un code qui compte le nombre de lignes de métro:

**La couche contient 2 lignes de métro distinctes : les lignes 1 et 2.**

```python
import geopandas as gpd

# Load the GeoJSON file
file_path = "/mnt/data/mobilite_et_transport_stations_metro.geojson"
gdf = gpd.read_file(file_path)

# Check unique metro lines in the dataset
unique_lines = gdf['ligne'].unique()
num_lines = len(unique_lines)
unique_lines, num_lines
```