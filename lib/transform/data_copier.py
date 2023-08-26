import os
import shutil

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def copy_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in sorted(os.walk(source_path)):
        for source_file_name in sorted(files):
            subdir = subdir.replace(f"{source_path}/", "")
            results_file_name = get_results_file_name(subdir, source_file_name)

            # Make results path
            os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

            source_file_path = os.path.join(source_path, subdir, source_file_name)
            results_file_path = os.path.join(results_path, subdir, results_file_name)

            # Check if file needs to be copied
            if clean or not os.path.exists(results_file_path):
                shutil.copyfile(source_file_path, results_file_path)

                if not quiet:
                    print(f"✓ Copy {results_file_name}")
            else:
                print(f"✓ Already exists {results_file_name}")


def get_results_file_name(subdir, source_file_name):
    if source_file_name == "gssa_2022_bezirke.csv":
        return "berlin-lor-health-and-structural-atlas-2022-00-districts.csv"
    if source_file_name == "gssa_2022_bezirksregionen.csv":
        return "berlin-lor-health-and-structural-atlas-2022-00-district-regions.csv"
    if source_file_name == "gssa_2022_planungsraeume.csv":
        return "berlin-lor-health-and-structural-atlas-2022-00-planning-areas.csv"
    if source_file_name == "gssa_2022_prognoseraeume.csv":
        return "berlin-lor-health-and-structural-atlas-2022-00-forecast-areas.csv"
    else:
        return source_file_name
