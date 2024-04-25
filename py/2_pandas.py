from pathlib import Path

import pandas as pd


measurements = Path("./measurements.txt")

df = pd.read_csv(measurements, sep=";", header=None, names=["city", "temp_value"])
df = df.groupby("city").agg(["min", "mean", "max"])
print(df)
