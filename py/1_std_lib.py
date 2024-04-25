from pathlib import Path

from tqdm import tqdm

measurements = Path("./measurements.txt")

cities = {}

with measurements.open() as file:
    for line in tqdm(file, total=1_000_000_000, unit_scale=True):
        city_name, temp_value = line.split(";")
        temp_value = float(temp_value)

        city_values = cities.get(
            city_name, {"count": 0, "sum": 0, "min": 500, "max": -500}
        )
        city_values["count"] += 1
        city_values["sum"] += temp_value
        city_values["min"] = min(city_values["min"], temp_value)
        city_values["max"] = max(city_values["max"], temp_value)
        cities[city_name] = city_values

for city_name, values in cities.items():
    mean = values["sum"] / values["count"]
    print(f"{city_name};{values['min']};{mean};{values['max']}")
