import json
import os
import unittest

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)

data_path = os.path.join(script_path, "..", "..", "data")

key_figure_group = "berlin-lor-health-and-structural-atlas"

statistic_properties = [
    "health_and_social_index",
    "employment_and_social_index",
    "working_life_sub_index",
    "social_status_sub_index",
    "health_sub_index"
]


class FilesTestCase(unittest.TestCase):
    pass


for year in [2013, 2022]:
    for half_year in ["00"]:
        for lor_area_type in ["districts", "forecast-areas", "district-regions", "planning-areas"]:
            file = os.path.join(data_path, f"{key_figure_group}-{year}-{half_year}",
                                f"{key_figure_group}-{year}-{half_year}-{lor_area_type}.geojson")
            setattr(
                FilesTestCase,
                f"test_{key_figure_group}_{year}_{half_year}_{lor_area_type}".replace('-', '_'),
                lambda self, file=file: self.assertTrue(os.path.exists(file))
            )


class PropertiesTestCase(unittest.TestCase):
    pass


for year in [2013, 2022]:
    for half_year in ["00"]:
        for lor_area_type in ["districts", "forecast-areas", "district-regions", "planning-areas"]:
            file = os.path.join(data_path, f"{key_figure_group}-{year}-{half_year}",
                                f"{key_figure_group}-{year}-{half_year}-{lor_area_type}.geojson")
            if os.path.exists(file):
                with open(file=file, mode="r", encoding="utf-8") as geojson_file:
                    geojson = json.load(geojson_file, strict=False)

                for feature in geojson["features"]:
                    feature_id = feature["properties"]["id"]
                    setattr(
                        PropertiesTestCase,
                        f"test_{key_figure_group}_{year}_{half_year}_{lor_area_type}_{feature_id}".replace('-', '_'),
                        lambda self, feature=feature: self.assertTrue(
                            all(property in feature["properties"] for property in statistic_properties))
                    )

if __name__ == '__main__':
    unittest.main()
