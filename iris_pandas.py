import pandas as pd


def main():

    iris_url = "https://j.mp/iriscsv"

    data = pd.read_csv(iris_url)
    
    data.columns = data.columns.str.upper()

    # some analysis params
    max_width_accepted = 4.20
    min_length_accepted = 6.9

    # the code below applies the "chaining commands" principle,
    # where the output of one action is immediately fed as input 
    # for the next opeation, meaning that at the end of the pipeline
    # the result corresponds to the sequence of provided commands
    # but all intermediate steps are discarded -> clean and efficient !

    analysis = (
        data
        # add columns
        # using a lambda ensures that we refer to the data at this point of the pipe
        .assign(OK_WIDTH = lambda df: df["SEPAL_WIDTH"] <= max_width_accepted)
        # remove columns
        .drop(columns=["SEPAL_WIDTH", "PETAL_WIDTH"])
        # groupby and aggregate
        .groupby("SPECIES")
        .agg({
            "SEPAL_LENGTH": "max",
            "PETAL_LENGTH":"min",
            "OK_WIDTH": "count"
        })
        # resetting index (if you want to keep it)
        .reset_index(drop=False)
        # renaming
        .rename(columns={
            "SEPAL_LENGTH": "MAX_SEPAL_LENGTH",
            "PETAL_LENGTH":"MIN_PETAL_LENGTH",
            "OK_WIDTH":"COUNT_OK_WIDTH"  
        })
        # filtering
        .query("MAX_SEPAL_LENGTH > @min_length_accepted")
    )

    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

    print(analysis)

    return 0


if __name__ == "__main__":
    main()