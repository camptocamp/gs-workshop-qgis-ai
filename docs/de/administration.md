---
outline: deep
---

# Administration

Sobald eine neue GeoNetwork-Instanz bereitgestellt wurde, ist es in der Regel eine gute Idee, mit dem Administrationsmodul zu beginnen.

## Status der Instanz überprüfen

### 1. Als Administrator anmelden

Verwende die Standard-Anmeldedaten `admin`/`admin`.

![Login menu](../assets/login.png)

### 2. Öffne das Dropdown-Menü „Administration“ und wähle „Statistiken und Status“

![Statistics and status](../assets/statistics-menu.png)

Dadurch gelangst du auf eine Seite, die den Status der verschiedenen GeoNetwork-Komponenten zusammenfasst.

### 3. Öffne den Tab „Informationen“

![Information tab](../assets/information-menu.png)

Die Informationsseite listet die verschiedenen Parameter auf, die in dieser Instanz verwendet werden. Diese Seite ist besonders nützlich, wenn Probleme wie Datenbankverbindungsfehler oder Speicherprobleme auf der Festplatte auftreten.

## Servereinstellungen

### 4. Öffne das Dropdown-Menü „Administration“ und wähle „Einstellungen“

![Settings](../assets/server-settings.png)

Hier findest du eine Liste mit Einstellungen, mit denen du das Verhalten von GeoNetwork konfigurieren kannst.

Einstellungen ermöglichen unter anderem:
* Änderung des öffentlichen Hosts und Ports für den Webzugriff auf die Instanz
* Konfiguration von SMTP für E-Mail-Benachrichtigungen
* Aktivierung von Nutzer-Feedback zu Katalogeinträgen
* Anpassung des Authentifizierungsprozesses (Selbstregistrierung, CAPTCHA, Passwortstärke...)
* INSPIRE-Konfiguration
* Verwaltung der Benutzerrechte
* usw.

## Verwaltung von Benutzern & Gruppen

### 5. Öffne das Dropdown-Menü „Administration“ und wähle „Benutzer und Gruppen“

![Users and groups](../assets/users-menu.png)

Hier kannst du Benutzer verwalten, die sich in der Instanz anmelden, sowie ihre Gruppen.

Erstelle eine neue Gruppe mit einem beliebigen Namen. Beachte, dass das „Name“-Feld später als Bezeichner verwendet wird – notiere es dir daher.

Als Nächstes erstelle einen neuen Benutzer und gewähre ihm alle verfügbaren Rechte in der neu erstellten Gruppe, mit Ausnahme des „Administrator“-Status. Gib ihm einen Login und ein Passwort, das du dir merken kannst.

## Portale

### 6. Gehe zurück zum Menü „Einstellungen“ und öffne den Tab „Quellen“

![Sources menu](../assets/sources-menu.png)

Dieser Bildschirm ermöglicht es unter anderem, „Sub-Portale“ zu erstellen. Ein Sub-Portal ist eine öffentliche Schnittstelle für deinen Katalog mit eigener Konfiguration. Dies kann z. B. verwendet werden, um nur Datensätze eines bestimmten Typs oder einer bestimmten Gruppe anzuzeigen.

### 7. Erstelle ein neues Sub-Portal, das nur Datensätze der neuen Gruppe anzeigt

Klicke auf „Portal hinzufügen“. Gib einen Namen und eine Kennung ein und setze den Suchfilter auf:

```
+groupPublished:"meinegruppe"
```


::: info
Ersetze `meinegruppe` durch die **Kennung** der erstellten Gruppe.
:::

![Source search filter](../assets/source-search-filter.png)

Dadurch wird sichergestellt, dass dieses neue Sub-Portal nur Datensätze anzeigt, die von der erstellten Gruppe veröffentlicht wurden.

Du kannst es über das Dropdown-Menü oben links aufrufen, allerdings wird möglicherweise noch ein Fehler angezeigt, da der Katalog noch nicht mit Datensätzen gefüllt ist.

## Verwaltung von Schlüsselwörtern

### 8. Öffne das Dropdown-Menü „Administration“ und wähle „Klassifikationssysteme“

![Classification menu](../assets/classification.png)

GeoNetwork bietet verschiedene Systeme zur Klassifikation. Dieses Menü ermöglicht den Zugriff auf:
* Thesaurus-Verwaltung
* Kategorien-Verwaltung

Kategorien werden in diesem Workshop nicht behandelt, da sie nicht essenziell sind.

Thesauri hingegen sind äußerst nützlich. Ein **Thesaurus** ist ein kontrolliertes Vokabular, das Schlüsselwörter (auch „Konzepte“ genannt) enthält. Schlüsselwörter werden zur Klassifizierung von Datensätzen verwendet und helfen Nutzern, schnell und effizient das zu finden, was sie suchen.

GeoNetwork unterstützt zwei Arten von Thesauri: **externe** und **lokale**.

### 9. Den GEMET-Thesaurus importieren

GEMET steht für _GEneral Multilingual Environmental Thesaurus_. Es ist ein weit verbreiteter Thesaurus. Durch den Import in deine GeoNetwork-Instanz erkennt GeoNetwork diese Schlüsselwörter in deinem Katalog und ermöglicht ihre Nutzung in Metadaten.

Um den GEMET-Thesaurus zu importieren, klicke auf „Thesaurus hinzufügen“ und dann auf „von URL“. Verwende folgende URL:

https://camptocamp.github.io/gs-workshop-geonetwork/gemet-theme.rdf

Klicke anschließend auf „Hochladen“. Danach sollte der GEMET-Themen-Thesaurus in der Liste erscheinen, und du kannst seinen Inhalt erkunden.

![GEMET themes](../assets/gemet-themes.png)

::: tip
Wie der Name schon sagt, sind die Schlüsselwörter dieses Thesaurus in mehreren Sprachen verfügbar!
:::

### 10. Einen lokalen Thesaurus erstellen

Ein lokaler Thesaurus ist für die eigene Bearbeitung gedacht und stammt nicht von offiziellen Stellen. Wir werden nun einen erstellen und ein Schlüsselwort hinzufügen.

Klicke erneut auf „Thesaurus hinzufügen“ und wähle diesmal „Neuer Thesaurus“. Vergib einen Namen, eine Beschreibung und eine Dateibezeichnung.

Schnell wirst du feststellen, dass dieser Thesaurus mehr Optionen bietet, z. B. das Ändern seines Namens und seiner Beschreibung sowie das Hinzufügen eigener Schlüsselwörter.

![New thesaurus](../assets/new-thesaurus.png)

Versuche, einige Schlüsselwörter hinzuzufügen – wir werden sie später verwenden.
