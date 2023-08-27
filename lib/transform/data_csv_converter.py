import os
import re

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):

        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        # Iterate over raw files
        for file_name in [file_name for file_name in sorted(files) if file_name.endswith("-raw.csv")]:
            source_file_path = os.path.join(source_path, subdir, file_name)
            convert_file_to_csv(source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)

    years = [2013, 2022]

    # Iterate over years
    for year in years:

        # Replace year in source file name
        file_path_csv = f"{source_file_name.replace('-raw', '')}.csv"
        file_path_csv = re.sub(r'\d{4}', str(year), file_path_csv)

        # Check if result needs to be generated
        if clean or not os.path.exists(file_path_csv):

            try:
                if source_file_name.endswith(f"-districts-raw"):
                    id_length = 2
                elif source_file_name.endswith(f"-forecast-areas-raw"):
                    id_length = 4
                elif source_file_name.endswith(f"-district-regions-raw"):
                    id_length = 6
                elif source_file_name.endswith(f"-planning-areas-raw"):
                    id_length = 8
                else:
                    id_length = 0

                if source_file_name.endswith(f"-districts-raw") \
                        or source_file_name.endswith(f"-forecast-areas-raw") \
                        or source_file_name.endswith(f"-district-regions-raw") \
                        or source_file_name.endswith(f"-planning-areas-raw"):

                    names = ["id", "name",
                             "health_and_social_index_2013", "health_and_social_index_2022",
                             "employment_and_social_index_2013", "employment_and_social_index_2022",
                             "working_life_sub_index_2013", "working_life_sub_index_2022",
                             "social_status_sub_index_2013", "social_status_sub_index_2022",
                             "health_sub_index_2013", "health_sub_index_2022"]
                    drop_columns = ["name"]

                    # Iterate over other years to remove them from data frame
                    for y in [y for y in years if y != year]:
                        drop_columns += [f"health_and_social_index_{y}", f"employment_and_social_index_{y}",
                                         f"working_life_sub_index_{y}", f"social_status_sub_index_{y}",
                                         f"health_sub_index_{y}"]

                else:
                    names = []
                    drop_columns = []

                dataframe = pd.read_csv(source_file_path, skiprows=1, names=names) \
                    .drop(columns=drop_columns, errors="ignore") \
                    .dropna() \
                    .assign(id=lambda x: x["id"].astype(str).str.zfill(id_length)) \
                    .rename(columns={
                        "id": "id",
                        f"health_and_social_index_{year}": "health_and_social_index",
                        f"employment_and_social_index_{year}": "employment_and_social_index",
                        f"working_life_sub_index_{year}": "working_life_sub_index",
                        f"social_status_sub_index_{year}": "social_status_sub_index",
                        f"health_sub_index_{year}": "health_sub_index"
                    })

                # Write csv file
                if dataframe.shape[0] > 0:
                    # Create directory if missing
                    directory, _ = os.path.split(file_path_csv)
                    os.makedirs(directory, exist_ok=True)

                    dataframe.to_csv(file_path_csv, index=False)
                    if not quiet:
                        print(f"✓ Convert {os.path.basename(file_path_csv)}")
                else:
                    if not quiet:
                        print(dataframe.head())
                        print(f"✗️ Empty {os.path.basename(file_path_csv)}")
            except Exception as e:
                print(f"✗️ Exception: {str(e)}")
        elif not quiet:
            print(f"✓ Already exists {os.path.basename(file_path_csv)}")
