from pathlib import Path

import ibis

measurements = Path("./measurements.txt")

con = ibis.connect("duckdb://")

df = con.read_csv(
    measurements, columns={"city": "VARCHAR", "temp_value": "FLOAT"}, sep=";"
)
df = df.group_by("city").aggregate(
    [df.temp_value.min(), df.temp_value.mean(), df.temp_value.max()]
)
print(df.to_pandas())
