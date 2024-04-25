from pathlib import Path

import ibis

measurements = Path("./measurements.txt")

con = ibis.dask.connect()

df = con.read_csv(measurements, sep=";", header=None, names=["city", "temp_value"])
df = df.group_by("city").aggregate(
    [df.temp_value.min(), df.temp_value.mean(), df.temp_value.max()]
)
print(df.to_pandas())
