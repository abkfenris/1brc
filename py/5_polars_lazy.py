from pathlib import Path

import polars as pl

measurements = Path("./measurements.txt")

df = pl.scan_csv(
    measurements,
    has_header=False,
    new_columns=["city", "temp_value"],
    separator=";",
)
df = df.group_by("city").agg(
    pl.col("temp_value").min().alias("min"),
    pl.col("temp_value").mean().alias("mean"),
    pl.col("temp_value").max().alias("max"),
)
print(df.collect())
