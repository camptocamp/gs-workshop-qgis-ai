---
outline: deep
---

# Adding Records

In this section we will populate our new, freshly set up GeoNetwork instance with some metadata records.

## Harvesting

The process called "harvesting" means automatically copying metadata records published on another platform using standard protocols. GeoNetwork supports a wide range of protocols, the most popular being CSW and OAI-PMH. Harvesting can be set up to run at fixed intervals, producing reports and even mail notifications according to the way GeoNetwork is set up.

In this workshop though, we would like to demonstrate how GeoNetwork is actually able to interface itself with many other platforms and APIs outside of the mainstream protocols used in the geospatial ecosystem.

For this reason we will now harvest an open data platform: https://open.nrw/.

This data platform is [running CKAN under the hood](https://open.nrw/open-data/informationen-fuer-entwicklerinnen-und-entwickler) so we can use its API to harvest records.

### 1. Open the Administration dropdown and select "Harvesting" 

![Harvesting](assets/harvesting.png)

### 2. Click on "Harvest from" and select "Simple URL"

The "Simple URL" harvester type is able to process most JSON-based APIs as well as some XML ones; its parameters can be adjusted so that it is able to understand different kinds of responses.

### 3. Set up & run the harvester

Give a name to the harvester and disable scheduling (otherwise it might run unexpectedly in the future).

![Simple URL harvester](assets/simple-url-harvester.png)

Next, use the following parameters for the harvester:
* URL: https://open.nrw/api/3/action/current_package_list_with_resources?limit=20  
  This points to the CKAN API
* Element to loop on: `/result`
* Element for the UUID of each record: `/id`
* Pagination parameters: `disabled`
* XSL transformation to apply: `schema:iso19115-3.2018:convert/fromJsonCkan`

![Harvester parameters](assets/harvester-parameters.png)

Then, click "Save"; the harvester is ready to use. You can now press "Harvest" at the top of the harvester panel: 20 new records should be added to your local catalog.

You can see them if you navigate to the "Search" page of the GeoNetwork interface and click on any of them to get more information.

## Importing (optional)

GeoNetwork allows exporting and importing multiple records in a packaged ZIP file containing the metadata as well as all associated files. This export format called "MEF" (Metadata Export Format) is practical because it works across multiple GeoNetwork versions.

For the purpose of this workshop a small export of the [BKG Geodaten Catalog](https://gdk.gdi-de.org/gdi-de) has been made.

### 4. Download the ZIP file containing the records

The ZIP file is stored here: [bkg-datasets.zip](/bkg-datasets.zip)

### 5. Open the Contribute dropdown and select "Import new records"

![Import new records](assets/import-records.png)

This will take you to a page offering several options for importing records: either by URL, copy-pasting XML, or uploading a ZIP file.

### 6. Select the file and import it

Choose the "Upload a file from your computer" and click on the green button to select the file you just downloaded.

![Upload from your computer](assets/upload-file-import.png)

Leave other options as they are and click on "Import" at the bottom of the page.

After a while you should see a message letting you know that 20 records were imported successfully. If you are curious, navigate to the search interface to see them!

![Successful import](assets/successful-import.png)
