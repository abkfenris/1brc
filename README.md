# 1brc
One Billion Row Challenge

Attempts at the [1 Billion Row Challenge](https://1brc.dev).

To get started `pixi run create_measurements` to generate 1 billion city temperature pairs (approximately 13 GB).

Environments and tasks are managed with [Pixi](https://pixi.sh/) for sanity.

## Rough results:

time (seconds) | `pixi run <task>` | description
---------------|-------------------|------------
776.58 s | [`py_1_std_lib`](./py/1_std_lib.py) | Just using the standard library (plus TQDM to keep track) and iterating over a file by lines
129.07 s | [`py_2_pandas`](py/2_pandas.py) | Pandas groupby and aggreggate
56.22 s | [`py_3_dask`](./py/3_dask.py) | Dask groupby and aggregate
error (locked up machine) | [`py_4_polars_eager`](./py/4_polars_eager.py) | Using Polar's eager or immediate Pandas-like API caused my computer to lock up
130.02 s | [`py_5_polars_lazy`](./py/5_polars_lazy.py) | Polars has a lazy API, though it wasn't much faster (though lower memeory) than Pandas as it couldn't skip reading data.
__9.27 s__ | [`py_6_1_ibis_duckdb`](./py/6_1_ibis_duckdb.py) | Ibis is a library that wrapps multiple ways of interacting with dataframes. The default way is to use DuckDB, which managed to read the file at around 1.5 GB/s!
