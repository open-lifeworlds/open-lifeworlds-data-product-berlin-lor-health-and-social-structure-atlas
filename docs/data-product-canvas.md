
# Data Product Canvas - Berlin LOR Health and Social Structure Atlas

## Metadata

* owner: Open Lifeworlds
* description: Data product providing Berlin health and social structure data on different LOR hierarchy levels
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-crime-atlas
* license: CC-BY 4.0
* updated: 2025-11-09

## Input Ports

### berlin-lor-geodata

* manifest URL: https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/refs/heads/main/data-product-manifest.yml

### berlin-health-and-social-structure-atlas-source-aligned

* manifest URL: https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-health-and-social-structure-atlas-source-aligned/refs/heads/main/data-product-manifest.yml

## Transformation Steps

* [Data extractor](https://github.com/open-lifeworlds/open-lifeworlds-python-lib/blob/main/openlifeworlds/extract/data_extractor.py) extracts data from inout ports
* [Data blender](https://github.com/open-lifeworlds/open-lifeworlds-python-lib/blob/main/openlifeworlds/transform/data_blender.py) blends csv data into geojson files

## Output Ports

### berlin-health-and-social-structure-atlas-geojson
name: Berlin Health And Social Structure Atlas Geojson
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/tree/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson
* license: CC-BY 4.0
* updated: 2025-11-09

**Files**

* [berlin-health-and-social-structure-atlas-2013-00-district-regions.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2013-00-district-regions.geojson)
* [berlin-health-and-social-structure-atlas-2013-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2013-00-districts.geojson)
* [berlin-health-and-social-structure-atlas-2013-00-forecast-areas.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2013-00-forecast-areas.geojson)
* [berlin-health-and-social-structure-atlas-2022-00-district-regions.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2022-00-district-regions.geojson)
* [berlin-health-and-social-structure-atlas-2022-00-districts.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2022-00-districts.geojson)
* [berlin-health-and-social-structure-atlas-2022-00-forecast-areas.geojson](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-geojson/berlin-health-and-social-structure-atlas-2022-00-forecast-areas.geojson)


### berlin-health-and-social-structure-atlas-statistics
name: Berlin Health And Social Structure Atlas Statistics
* owner: Open Lifeworlds
* url: https://github.com/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/tree/main/data/03-gold/berlin-health-and-social-structure-atlas-statistics
* license: CC-BY 4.0
* updated: 2025-11-09

**Files**

* [berlin-health-and-social-structure-atlas-statistics.json](https://media.githubusercontent.com/media/open-lifeworlds/open-lifeworlds-data-product-berlin-health-and-social-structure-atlas/refs/heads/main/data/03-gold/berlin-health-and-social-structure-atlas-statistics/berlin-health-and-social-structure-atlas-statistics.json)


## Observability

### Quality metrics

 * name: geojson_property_completeness
 * description: The percentage of geojson features that have all necessary properties

| Name | Value |
| --- | --- |
| berlin-health-and-social-structure-atlas-2013-00-districts.geojson | 100 |
| berlin-health-and-social-structure-atlas-2013-00-forecast-areas.geojson | 98 |
| berlin-health-and-social-structure-atlas-2013-00-district-regions.geojson | 99 |
| berlin-health-and-social-structure-atlas-2013-00-forecast-areas.geojson | 98 |
| berlin-health-and-social-structure-atlas-2022-00-districts.geojson | 100 |
| berlin-health-and-social-structure-atlas-2022-00-forecast-areas.geojson | 98 |
| berlin-health-and-social-structure-atlas-2022-00-district-regions.geojson | 99 |
| berlin-health-and-social-structure-atlas-2022-00-forecast-areas.geojson | 98 |


## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

consumer-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).