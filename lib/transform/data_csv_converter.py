import os

import pandas as pd

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def convert_data_to_csv(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):

        # Make results path
        subdir = subdir.replace(f"{source_path}/", "")
        os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

        for file_name in sorted(files):
            source_file_path = os.path.join(source_path, subdir, file_name)
            convert_file_to_csv(source_file_path, clean=clean, quiet=quiet)


def convert_file_to_csv(source_file_path, clean=False, quiet=False):
    source_file_name, source_file_extension = os.path.splitext(source_file_path)
    file_path_csv = f"{source_file_name.replace('-raw', '')}.csv"

    # Check if result needs to be generated
    if clean or not os.path.exists(file_path_csv):
        if not source_file_path.endswith("-raw.csv"):
            return

        year = os.path.basename(source_file_name).split(sep="-")[6]
        half_year = os.path.basename(source_file_name).split(sep="-")[7]

        # Set default values
        drop_columns = []

        try:
            if source_file_name.endswith(f"{year}-{half_year}-districts-raw") :
                id_length = 2
            elif source_file_name.endswith(f"{year}-{half_year}-forecast-areas-raw"):
                id_length = 4
            elif source_file_name.endswith(f"{year}-{half_year}-district-regions-raw"):
                id_length = 6
            elif source_file_name.endswith(f"{year}-{half_year}-planning-areas-raw"):
                id_length = 8
            else:
                id_length = 0

            if source_file_name.endswith(f"{year}-{half_year}-districts-raw") \
                    or source_file_name.endswith(f"{year}-{half_year}-forecast-areas-raw") \
                    or source_file_name.endswith(f"{year}-{half_year}-district-regions-raw") \
                    or source_file_name.endswith(f"{year}-{half_year}-planning-areas-raw"):

                names = ["id", "name",
                         "health_and_social_index_2013", "health_and_social_index_2022",
                         "employment_and_social_index_2013", "employment_and_social_index_2022",
                         "working_life_sub_index_2013", "working_life_sub_index_2022",
                         "social_status_sub_index_2013", "social_status_sub_index_2022",
                         "health_sub_index_2013", "health_sub_index_2022"]
                drop_columns = ["name"]
            else:
                names = []
                drop_columns = []

            dataframe = pd.read_csv(source_file_path, skiprows=1, names=names) \
                .drop(columns=drop_columns, errors="ignore") \
                .dropna() \
                .assign(id=lambda x: x["id"].astype(str).str.zfill(id_length))

            # Write csv file
            if dataframe.shape[0] > 0:
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
