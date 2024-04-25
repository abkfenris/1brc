from pathlib import Path

import dask.dataframe as dd


measurements = Path("./measurements.txt")

df = dd.read_csv(measurements, sep=";", header=None, names=["city", "temp_value"])
df = df.groupby("city").agg(["min", "mean", "max"])
df = df.compute()
print(df)
