import re
from pathlib import Path


def group_measurements_by_key(path: Path):
    regex_pattern = r"^(\d{4})_(.+)_(.+)\.csv$"

    grouped_files = {}

    if not path.is_dir():
        return grouped_files

    for file_path in path.iterdir():
        if file_path.is_file():
            match = re.match(regex_pattern, file_path.name)

            if match:
                rok, wielkosc, czestotliwosc = match.groups()
                key = (rok, wielkosc, czestotliwosc)
                grouped_files[key] = file_path

    return grouped_files


def main():
    grouped_files = group_measurements_by_key(Path('./measurements'))
    for key, value in grouped_files.items():
        print(key, value)


if __name__ == "__main__":
    main()