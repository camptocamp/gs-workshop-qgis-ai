---
outline: deep
---

# Common Issues

## I'm getting the error "Index cannot be found"

Something must be wrong in the way GeoNetwork was set up, specifically the host and port that was given to connect to ElasticSearch. Make sure that the correct ElasticSearch host and port were given when starting GeoNetwork, and that ElasticSearch is indeed running without errors.

## GeoNetwork does not start

There are multiple potential reasons for this:
* Database connection failed
* Incorrect Java version
* Corrupt database for which a migration job is failing

## Every time I open the search interface an error shows up

You can try reindexing the records in the Administration/Tools menu. If it doesn't work, try deleting and recreating the index (2nd option).

## I keep getting an error even after having added records

Try creating a new set of User Interface Settings in the Administration/Settings menu:

![Create UI settings](assets/create-ui-settings.png)

Remember to save the settings once created.

## Something's not working with my Docker containers

The following command will show you the logs of what is going on inside the Docker composition:

```shell
docker compose logs -f
```

To stop printing the logs in the terminal, press CTRL+C.
