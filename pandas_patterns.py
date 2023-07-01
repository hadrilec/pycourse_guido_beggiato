from datetime import date, timedelta

import numpy as np
import pandas as pd


def setup_df() -> pd.DataFrame:
    """generate a basic df for the examples"""
    size = 10
    df = pd.DataFrame()
    df["LETTER"] = [x.upper() for x in "abcdefghij"]
    df["ID"] = list(range(size))
    today = date.today()
    df["DATE"] = [today+timedelta(days=d%3) for d in range(size)]
    return df


def standard():
    """plain solution"""
    df = setup_df()
    
    ### filtering
    min_id = 5
    df2 = df[df["ID"] >= min_id]

    # df2 is actually a "view" on df -> any modifications to
    # df2 WILL be reflected on df: we may not want that ("SettingWithCopyWarning")

    ### creating new columns from starting one
    # if ID is even -> keep it, else -> set it to 0
    df["NEW_COL"] = np.where(df["ID"]%2==0, df["ID"], 0)

    ### groupby
    group = df.groupby("DATE")
    df = group.agg({"NEW_COL": "sum"})
    df = df.reset_index()

    print(df)


def native():
    """pandas native"""
    df = setup_df()

    ### filtering
    min_id = 5
    df2 = df.query("ID >= @min_id")
    # df2 is a fully distinc and independent object from df 
    # plus, this method can be chained

    ### creating new columns from starting one
    # if id is even -> keep it, else -> set it to 0
    df["NEW_COL"] = df["ID"].where(df["ID"]%2==0, 0)
    # availble also with "assign" (for chaining !)
    # as we are using a lambda function, you may not get editor hints
    df = df.assign(NEW_COL = lambda df: df["ID"].where(df["ID"]%2==0, 0))

    ### groupby
    df = (
        df
        # for speed in grouping, not really
        # needed and available in the above as well
        .assign(DATE = lambda df: df["DATE"].astype("category")) 
        .groupby("DATE", as_index=False)
        .agg({"NEW_COL": "sum"})
    )

    print(df)


def both():
    """summary comparison of the 2 pipelines styles"""

    # parameters used in the analysis
    min_id = 5

    # standard
    df = setup_df()
    min_id = 5
    df = df[df["ID"] >= min_id]
    df["NEW_COL"] = np.where(df["ID"]%2==0, df["ID"], 0)
    df["DATE"] = df["DATE"].astype("category")
    group = df.groupby("DATE")
    df = group.agg({"NEW_COL": "sum"})
    standard = df.reset_index()
    
    # pandas' style
    native = (
        setup_df()
        .query("ID >= @min_id")
        # NOTE: this "df" is NOT the same of 
        # above, it's just the name of the
        # param of the lambda function
        #                         |
        #                         V
        .assign(
            NEW_COL = lambda df: df["ID"].where(df["ID"]%2==0, 0),
            DATE = lambda df: df["DATE"].astype("category")
        )  
        .groupby("DATE", as_index=False)
        .agg({"NEW_COL": "sum"})
    )

    print(standard)
    print(standard.equals(native)) # True


    # we can see we get the same result in both ways,
    # however the second one 
    #   is clearer
    #   uses only pandas and not other libraries
    #   creates a single variable: 
    #       no doubts about where data is
    #       memory efficient
    #       easily recyclable if put inside a function
    #   since every method creates a NEW dataframe, the inputs are NOT modified -> they can be reused safely    



if __name__ == "__main__":
    _ = system("cls")
    both()