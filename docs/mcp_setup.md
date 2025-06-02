---
outline: deep
---

# Utilisation du protocole MCP

## Introduction

Nous allons installer le plugin [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) puis l'utiliser depuis des clients MCP comme Claude Desktop ou depuis des extensions VS Code comme Cline ou Continue.

## Fonctionnement

Le plugin QGIS MCP ouvre une socket sur le port 9876. Puis lorsqu'il reçoit des requêtes, il lance les commandes adéquates dans QGIS et renvoie une indication de succès ou le message d'erreur. Cette socket évite d'avoir à installer des dépendances supplémentaires dans l'environnement de QGIS.

Puis nous lancerons un serveur MCP, ce serveur est un client pour la socket du plugin QGIS, mais aussi un serveur du point de vue du client MCP (utilisation de stdin/stdout).

Enfin nous lancerons un agent conversationnel. Cet agent fera donc le lien entre l'utilisateur, le LLM et le serveur MCP.

Lors d'une demande de l'utilisateur, l'agent transmet au LLM, en plus de la demande de l'utilisateur, la liste des actions disponibles sur le serveur MCP. Le LLM sera donc en capacité d'établir un plan d'exécution pour répondre à la demande.

Lors de la réponse du LLM, l'agent se charge d'éxécuter les actions choisies par le LLM en utilisant le serveur MCP, puis renverra les informations obtenues au LLM, et ainsi de suite jusqu'à réussir à répondre à la demande de l'utilisateur.

## Installation du plugin et du serveur MCP

### Installer le plugin QGIS

- Installer le plugin MCP depuis le gestionnaire de plugins de QGIS.

- Cliquer sur le bouton QGIS MCP dans la barre d'outil des plugins puis démarrer le serveur.

A noter vous pouvez également utiliser la variable `QGIS_PLUGINPATH` pour utiliser le code source du plugin de l'étape suivante.

### Installer le serveur MCP

Installer git : https://git-scm.com/downloads/win

```bash
git clone https://github.com/jjsantos01/qgis_mcp.git
```

Ou télécharger les sources : https://github.com/jjsantos01/qgis_mcp/archive/refs/heads/main.zip

Pour faire fonctionner le serveur MCP nous aurons besoin d'installer `uv`.

Windows et MacOS : https://github.com/jjsantos01/qgis_mcp?tab=readme-ov-file#installation

Linux : https://github.com/astral-sh/uv?tab=readme-ov-file#installation

Tester le serveur :

```bash
uv --directory "/ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp" run qgis_mcp_server.py
```

<!--
uv --directory "qgis_mcp/src/qgis_mcp" run qgis_mcp_server.py
-->

### Configurer Claude Desktop (Windows et MacOS only)

Installer et lancer Claude Desktop :

Aller dans : `Ficher > Paramètres > Développeur > Modifier la configuration`

Et ajouter la configuration :

<!--
`%UserProfile%\AppData\Roaming\Claude\claude_desktop_config.json`
-->

```json
{
	"mcpServers": {
        "qgis": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp",
                "run",
                "qgis_mcp_server.py"
            ]
        }

    }
}
```

::: warning
Attention sous Windows pensez à doubler les '\', exemple :

`"G:\\qgis-ai-workshop\\qgis_mcp\\src\\qgis_mcp"`
:::

Dans Paramètres > Général > Paramètres de Claude > Configurer, puis dans les Paramètres > Intégrations vous devriez maintenant voir QGIS et pouvoir afficher la liste des actions disponibles pour QGIS avec le bouton ... > Outils et paramètres.

Pour tester le fonctionnement, démarrez une conversation avec :

```text
Quelles sont les couches chargées dans QGIS ?
```

Liens : https://github.com/jjsantos01/qgis_mcp?tab=readme-ov-file#claude-for-desktop-integration


### Configurer Cline

Dans VS Code, installez l'extension Cline.

Dans le menu `View > Open View` ouvrez la side bar de Cline.

Choisissez un fournisseur de modèles de langage et entrez une clé d'API.

Ajoutez un serveur MCP, icône en forme de rack de serveurs, puis onglet Installed

Ajouter dans le fichier `cline_mcp_settings.json` :

<!--
Windows : C:\Users\Arnaud\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json

Linux : /home/amorvan/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
-->

```json
{
  "mcpServers": {
    "qgis": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp",
        "run",
        "qgis_mcp_server.py"
      ]
    }
  }
}
```

::: warning
Attention, sous Windows utiliser des `/` et non des `\\` exemple :

`"G:/qgis-ai-workshop/qgis_mcp/src/qgis_mcp"`
:::

Pour tester le fonctionnement, démarrez une conversation avec :

```text
Quelles sont les couches chargées dans QGIS ?
```

::: tip
Il pourrait être nécessaire de redémarrer le serveur dans QGIS.
:::


## Configure Continue

Dans VS Code, installez l'extension Continue.dev.

Dans le menu `View > Open View` ouvrez la side bar de Continue.

Sous l'invite de chat, choisissez Agent à la place Chat.

Puis sélectionnez un modèle de langage et un clé d'API.

Ajouter un serveur MCP avec la configuration :

```yaml
name: New mcpServer
version: 0.0.1
schema: v1
mcpServers:
  - name: QGIS
    command: uv
    args:
      - "--directory"
      - "/ABSOLUTE/PATH/TO/PARENT/REPO/FOLDER/qgis_mcp/src/qgis_mcp"
      - "run"
      - "qgis_mcp_server.py"
    env: {}
```

Il est également possible d'ajouter des liens vers les différentes documentations de QGIS (doc utilisateur, API, Cookbook) pour les utiliser facilement plus tard en tant que contextes.
