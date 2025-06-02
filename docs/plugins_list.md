---
outline: deep
---

# Liste des plugins QGIS de Chatbot intégrés 


https://plugins.qgis.org/plugins/aino-qgis-plugin-main/

- Téléchargement de données OSM
- L'agent est payant


https://plugins.qgis.org/plugins/kue-ai

- Assistant
- L'agent est payant (19€ par mois / 1 mois gratuit)


https://plugins.qgis.org/plugins/qgpt_agent_release

- Assistant
- Uniquement compatible OpenAI
- Fait une erreur avec ma clé OpenAPI
- L'interface semble un peu brouillon pour l'instant


https://plugins.qgis.org/plugins/intelli_geo/

```bash
pip3 install --user /home/amorvan/.local/share/QGIS/QGIS3/profiles/default/python/plugins/intelli_geo/ -r requirements.txt
```

- Nécessite une clé d'API pour OpenAI
- L'interface n'est pas très intuitive, pas de streaming, lent à répondre.
- Ne répond que sous forme de code, toolbox (et Model builder, mais il est grisé).
+ Intéressant d'avoir une case à cocher toolbox / algorithme
+ Un bouton permet d'ouvrir le code directement dans l'éditeur python (liste déroulante à gauche)


https://plugins.qgis.org/plugins/promptly/

+ Interface chatbot avec onglets code.
+ Plusieurs modèles : OpenAI, Ollama, OpenRouteur, Anthopic, custom endpoint
- pas de coloration syntaxique
- pas d'historique de conversation


https://github.com/jjsantos01/qgis_mcp

+++ Utilisable depuis tous les agent qui supportent MCP
+++ Sécurité : L'utilisation du protocole MCP permet de proposer de nombreuses possibilités sans exécuter de code généré par les LLM. La LLM ne fait que choisir les fonctions à appeler et les valeurs des paramètres.
- Nécessite un client et de la configuration
- Impossible de customiser l'interface

Idées d'améliorations :
- Ouvrir le code dans l'éditeur Python de QGIS plutôt que de le lancer avec la méthode execute_code.
- Pouvoir récupérer l'image du canvas pour ajuster les styles.
