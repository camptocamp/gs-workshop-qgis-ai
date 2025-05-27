---
outline: deep
---

# Deploying the Datahub

In this section we will amend the existing docker composition.

### 1. Open the `docker-compose.yml` file and add the Datahub image

Add the following lines to the `docker-compose.yml` file we created earlier:

```yaml
  datahub:
    image: geonetwork/geonetwork-ui-datahub:2.4.4
    depends_on:
      geonetwork:
        condition: service_healthy
    volumes:
      - ./configuration/:/usr/share/nginx/html/datahub/assets/configuration
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.datahub.rule=Host(`localhost`) && PathPrefix(`/datahub`)"
      - "traefik.http.routers.datahub.entrypoints=web"
```

### 2. Copy the configuration file

Download the configuration file provided with this workshop here: <a target="_blank" href="/gs-workshop-geonetwork/default.toml">default.toml</a>. Put this file as is in a folder named `configuration` in the same folder as the `docker-compose.yml` file.

### 3. Start the Datahub container

**Stop any running command with CTRL+C.**

Run the following command on a terminal inside the workshop folder:

```shell
docker compose up -d
```

The Datahub application should be accessible on http://localhost:8080/datahub/

### 4. Customize the configuration

Open the `default.toml` file in the `configuration` folder that you downloaded and that is being read by the Datahub. You will find in it many parameters: feel free to tweak them!

A more complete customizing guide is available here: https://geonetwork.github.io/geonetwork-ui/main/docs/guide/configure.html

Things that can be controlled in the configuration:
* Theming: colors, background image...
* Changing the advanced filters
* Creating predefined searches
* Enabling multiple languages
* Customizing translations
* Changing the background layers of the map
* etc.

### 5. Enable authentication

Some features of the Datahub are only available when authenticated on GeoNetwork:
* Marking records as favorites
* Adding feedbacks on records

To allow logging in to GeoNetwork we first need to disable CSRF protection GeoNetwork.

::: warning
This should not be done on a production instance! CSRF protection fills a very important role in keeping users safe.

Please refer to this guide for how to handle this in production: https://geonetwork.github.io/geonetwork-ui/main/docs/guide/deploy.html#authentication
:::

**First, stop any running command with CTRL+C.**

Then, run the following command:

```shell
docker compose exec geonetwork bash -c "sed -i 's#<ref bean=\"csrfFilter\" />##' /opt/geonetwork/WEB-INF/config-security/config-security-core.xml
```

Finally, restart GeoNetwork:

```shell
docker compose restart geonetwork
```

### 6. Log in and set a record as favorite

Go back to the Datahub interface on http://localhost:8080/datahub/.

On each record there is a "star" icon; hovering it will offer you a login link. Click on it and enter the credentials of the user you created earlier.

You should be taken back to the Datahub. Now you will be able to set records as favorites, filter on your favorites only and even sort records by amount of people that set these records as favorites!
