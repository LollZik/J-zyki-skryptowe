import csv
import re
from pathlib import Path

def get_addresses(path: Path, city: str):

    addresses = []
    address_pattern = r"^(.*?)\s*(\d+[A-Za-z0-9\-/]*)?$"

    try:
        with open(path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row['Miejscowość'].strip().lower() == city.strip().lower():
                    wojewodztwo = row['Województwo']
                    miasto = row['Miejscowość']
                    pelny_adres = row['Adres']

                    ulica, numer = None, None

                    if pelny_adres:
                        match = re.match(address_pattern, pelny_adres)
                        if match:
                            ulica, numer = match.groups()
                            ulica = ulica.strip() if ulica else None
                        else:
                            ulica = pelny_adres

                    addresses.append((wojewodztwo, miasto, ulica, numer))

    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku {path}")

    return addresses


def main():
    addresses = get_addresses(Path('./stacje.csv'), 'Trzebnica')
    for address in addresses:
        print(address)

if __name__ == "__main__":
    main()