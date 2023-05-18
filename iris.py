from concurrent.futures import ThreadPoolExecutor as ThreadPool
from itertools import repeat, product, combinations_with_replacement
from os import system
from pathlib import Path
from pprint import pprint
from random import choices, randint
from time import perf_counter
from typing import Any, Callable, Iterable

from pandas import DataFrame as PandasDF, read_csv


def main():
    _ = system("cls")

    iris_url = "https://j.mp/iriscsv"
    iris_url = (Path(__file__).parent.parent / "iris.txt").read_text()

    data = read_csv(iris_url)
    data.columns = data.columns.str.upper()

    # some analysis params
    max_width_accepted = 4.20
    min_length_accepted = 6.9

    analysis = (
        data
        # add columns
        .assign(OK_WIDTH=data["SEPAL_WIDTH"] <= max_width_accepted)
        # remove columns
        .drop(columns=["SEPAL_WIDTH", "PETAL_WIDTH"])
        # groupby and aggregate
        .groupby("SPECIES")
        .agg({
            "SEPAL_LENGTH": "max",
            "PETAL_LENGTH":"min"
        })
        # resetting index (if you want to keep it)
        .reset_index(drop=False)
        # renaming
        .rename(columns={
            "SEPAL_LENGTH": "MAX_SEPAL_LENGTH",
            "PETAL_LENGTH":"MIN_PETAL_LENGTH" 
        })
        # filtering
        .query("MAX_SEPAL_LENGTH > @min_length_accepted")
    )

    print(analysis)
  



    

    return 0


if __name__ == "__main__":
    main()