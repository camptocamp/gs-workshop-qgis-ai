---
outline: deep
---

# Introduction

Maintenant que nous avons mis en place un Agent avec le serveur MCP qui communique avec QGIS nous allons tester des scénarios de conversations plus ou moins complexes.

# Uses cases

## Tester le fonctionnement

_Quelle est ma version de QGIS ?_

## Ajouter une couche

_Peux-tu ajouter dans QGIS la couche MNT france entière qui se trouve quelque part dans ~/data/IGN ?_

## Créer un style

_Peux-tu me changer le style de la couche département pour afficher les noms de département dans les étiquettes ?_

_Dans QGIS j'ai chargé 5 couches, pourrait tu me faire des styles cohérents en fonction des échelles, avec de la transparence et des étiquettes avec les champs NOM_

::: info
Problème : il est nécessaire de faire récupérer une entité pour obtenir la liste des champs et les géométries font exploser le contexte, il faudrait pouvoir récupérer uniquement la liste des champs, ou un feature sans geometrie.
:::

## Modifier le plugin MCP lui-même

Afin de donner la possibilité à l'agent conversationnel de récupérer la liste des champs d'une couche, nous allons maintenant ajouter dans le plugin QGIS MCP :
- une action dans le serveur MCP
- la méthode associée dans le plugin QGIS

Ouvrer le code du plugin dans VS Code :

```bash
code .../qgis_mcp
```

Et donner à Cline l'instruction suivante :

_Pourrais tu ajouter une action dans le serveur MCP et dans le plugin QGIS pour récupérer la liste des champs d'une couche ?_

Après plusieurs échanges avec le LLM, Cline devrait vous proposer les modifications suivantes :

```diff
diff --git a/qgis_mcp_plugin/qgis_mcp_plugin.py b/qgis_mcp_plugin/qgis_mcp_plugin.py
index d7e649a..0efd859 100644
--- a/qgis_mcp_plugin/qgis_mcp_plugin.py
+++ b/qgis_mcp_plugin/qgis_mcp_plugin.py
@@ -142,6 +142,7 @@ class QgisMCPServer(QObject):
                 "remove_layer": self.remove_layer,
                 "zoom_to_layer": self.zoom_to_layer,
                 "get_layer_features": self.get_layer_features,
+                "get_layer_fields": self.get_layer_fields,
                 "execute_processing": self.execute_processing,
                 "save_project": self.save_project,
                 "render_map": self.render_map,
@@ -374,6 +375,20 @@ class QgisMCPServer(QObject):
             }
         else:
             raise Exception(f"Layer not found: {layer_id}")
+
+    def get_layer_fields(self, layer_id, **kwargs):
+        """
+        Retourne la liste des champs d'une couche vectorielle à partir de son identifiant.
+        :param layer_id: identifiant de la couche (str)
+        :return: liste des noms de champs
+        """
+        project = QgsProject.instance()
+        if layer_id not in project.mapLayers():
+            raise Exception(f"Layer not found: {layer_id}")
+        layer = project.mapLayer(layer_id)
+        if layer.type() != QgsMapLayer.VectorLayer:
+            raise Exception(f"Layer is not a vector layer: {layer_id}")
+        return [field.name() for field in layer.fields()]
     
     def execute_processing(self, algorithm, parameters, **kwargs):
         """Execute a processing algorithm"""
@@ -437,7 +452,7 @@ class QgisMCPServer(QObject):
             }
         else:
             raise Exception(f"Failed to save project to {path}")
-    
+
     def render_map(self, path, width=800, height=600, **kwargs):
         """Render the current map view to an image"""
         try:
diff --git a/src/qgis_mcp/qgis_mcp_server.py b/src/qgis_mcp/qgis_mcp_server.py
index 9f5e325..bcdc0ab 100644
--- a/src/qgis_mcp/qgis_mcp_server.py
+++ b/src/qgis_mcp/qgis_mcp_server.py
@@ -226,6 +226,17 @@ def get_layer_features(ctx: Context, layer_id: str, limit: int = 10) -> str:
     result = qgis.send_command("get_layer_features", {"layer_id": layer_id, "limit": limit})
     return json.dumps(result, indent=2)
 
+@mcp.tool()
+def get_layer_fields(ctx: Context, layer_id: str) -> str:
+    """
+    Récupère la liste des champs d'une couche vectorielle à partir de son identifiant.
+    :param layer_id: identifiant de la couche (str)
+    :return: liste des noms de champs
+    """
+    qgis = get_qgis_connection()
+    result = qgis.send_command("get_layer_fields", {"layer_id": layer_id})
+    return json.dumps(result, indent=2)
+
 @mcp.tool()
 def execute_processing(ctx: Context, algorithm: str, parameters: dict) -> str:
     """Execute a processing algorithm with the given parameters."""
```

Acceptez les modifications.

Testez la nouvelle action.

::: tip
Il pourrait être nécessaire de :

- Recharger le plugin QGIS MCP et relancer le serveur.
- Redémarrer le serveur MCP dans votre agent conversationnel.

Pour recharger facilement un plugin QGIS il peut être intéressant d'intaller le plugin nommé "Plugin Reloader".
:::

Ouvrez une nouvelle conversation, pour ne par surcharger inutilement le contexte du LLM et donner les intructions :

_Peux tu me récupérer la liste des champs de la couche départements ?_

Après plusieurs échanges avec le LLM, Cline devrait vous répondre avec la liste des champs de votre couche :

::: info
Task Completed

Voici la liste des champs de la couche "DEPARTEMENT" :

- ID_GEOFLA
- CODE_DEPT
- NOM_DEPT
- CODE_CHF
- NOM_CHF
- X_CHF_LIEU
- Y_CHF_LIEU
- X_CENTROID
- Y_CENTROID
- CODE_REG
- NOM_REGION
:::

## Créer un plugin

_Sachant que nous avons ici un plugin minimal pour QGIS : https://github.com/wonder-sk/qgis-minimal-plugin, je voudrais que tu me créer ici un dossier avec un plugin qui trie les couches, raster en bas, puis polygones, puis lignes et points._

<!--
_Je viens de créer `qgis_sort_layers_plugin` peux-tu m'ajouter un makefile pour le charger facilement dans QGIS avec un lien symbolique._
-->
