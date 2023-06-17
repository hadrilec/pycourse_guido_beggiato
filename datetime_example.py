# https://docs.python.org/3/library/datetime.html

from datetime import date, timedelta

import numpy as np
import pandas as pd


def main():
    # 3 ways of creating a date object

    ## automatic
    today = date.today()
    print(today) # 2023-06-17

    ## from a string in particular format
    day_from_string = date.fromisoformat("2021-03-09") # 2021-03-09
    print(day_from_string)

    ## using the official constructor
    reference_day = date(2022, 10, 1)
    print(reference_day.strftime("%Y-%b-%d")) # 2022-Oct-01

    # -----------------------------------------

    # many useful methods and attributes
    print(reference_day.year) # 2022 
    print(reference_day.month) # 10 [1-12]
    print(reference_day.day) # 1 [1-31]

    print(reference_day.weekday()) # 5, [0-6] (Monday-Sunday)

    # -----------------------------------------

    # you can do maths with dates !

    ## comparison
    print(today < reference_day) # False

    ### now we compare 2 strings
    today_str = today.isoformat()
    reference_day_str = reference_day.isoformat()
    print(today_str < reference_day_str) # False

    # this gives false as well, but it works ONLY because
    # in python the character representing '2' comes before the 
    # one representing '3'

    # comparison across strings goes 'letter by letter',
    # so in this case is as follows
    # -> 2 == 2
    # -> 0 == 0
    # -> 2 == 2
    # -> 3 != 2 -> comparison breaks here and you get the false

    # why compare strings when you can compare objects
    # that have been designed to represent dates and have
    # *dedicated* comparison methods ?

    # ... if you need the string version of your 
    # date, just use the 'toisoformat()' method !

    # comparison across dates is:
    # first compare the year, then month, then day
    # not only this is faster, it's also safer (comparing integers in
    # an objective concept, comparing strings is not -> alphabetical order
    # is just a convention!)

    # finally, a date represented as a string occupies roughly 3 times 
    # more space than a datetime object -> this starts to matter when you have
    # many of them into a pandas column ! 

    ## deltas in time

    days_in_between = today - reference_day
    print(type(days_in_between)) # class "datetime.timedelta" 

    # timedelta object represents the difference between 2 dates
    # it has a nice attribute named 'days' to quantify that
    n_days_in_between = days_in_between.days
    print(n_days_in_between) # int

    # -----------------------------------------

    # all the things we get for free with the datetime module
    # open the door to many **automatization** algorithms!
    
    # please see some examples below
    
    d = previous_sunday()
    print(d)

    d = go_back_100_days(date(2023, 4, 1))
    print(d)

    d1, d2 = get_time_window(7)
    print(f"{d1} -> {d2}")

        
def previous_sunday(reference_day:date=None) -> date:
    """
    given a date, returns the previous sunday
    if date is not provided, uses today as reference point
    input date is sunday, return input and not the previous sunday
    """
    # handle the default algorithm
    if reference_day is None:
        reference_day = date.today()
    # check input sanity
    if not isinstance(reference_day, date):
        raise TypeError(f"'reference_day' must be date, got {type(reference_day)}")
    # actually perform the algorithm
    for i in range(7):
        possible_sunday = reference_day.replace(day=reference_day.day-i)
        if possible_sunday.weekday() == 6:
            return possible_sunday


def go_back_100_days(reference_day:date=None) -> date:
    """
    given a date, returns the day that was 100 days before
    if date is not provided, uses today as reference point
    """
    if reference_day is None:
        reference_day = date.today()
    if not isinstance(reference_day, date):
        raise TypeError(f"'reference_day' must be date, got {type(reference_day)}")

    days_back = timedelta(days=100)
    return reference_day - days_back


def get_first_day_of_year(reference_day:date) -> date:
    """returns first day of the year of the provided day"""
    if not isinstance(reference_day, date):
        raise TypeError(f"'day' must be date, got {type(reference_day)}")
    return date(reference_day.year, 1, 1)


def get_time_window(n_days:int) -> tuple[date, date]:
    """
    given the dimension of a time window, gives
    back 2 dates: the first day of the current year
    and the day 'n_days' after that
    """
    if not isinstance(n_days, int):
        raise TypeError(f"'n_days' must be int, got {type(n_days)}")
    today = date.today()
    first = get_first_day_of_year(today)
    delta = timedelta(days=n_days)
    second = first + delta
    return (first, second)


def pandas_example():

    N = 1<<9
    FMT = "%Y-%m-%d"
    rand = np.random.RandomState(seed=1234)

    start_date = date.today()
    end_date = start_date + timedelta(days=N-1)

    df = pd.DataFrame()
    df["DATES"] = pd.date_range(
        start=start_date, 
        end=end_date, 
        freq=timedelta(days=1)
    )
    df["FLOW"] = rand.normal(size=N)
    df["DATES_AS_STRINGS"] = df["DATES"].dt.strftime(FMT)
    df["STRING_SLICE"] = df["DATES_AS_STRINGS"].str.slice(stop=4)
    df["YEAR"] = df["DATES"].dt.year
    df["QUARTER"] = df["DATES"].dt.quarter.astype("category")
    
    print(df.head(4), end="\n\n")
    print(df.dtypes, end="\n\n")

    grouped = (
        df
        .groupby(["YEAR", "QUARTER"], sort=True)
        .agg(
            FLOW_MEAN = ("FLOW", "mean"),
            FLOW_SUM = ("FLOW", "sum"),
            FLOW_MEDIAN = ("FLOW", "median")
        )
        # .reset_index()
    )
    print(grouped, end="\n\n")

    grouped = (
        df
        .groupby(
            pd.Grouper(
                key="DATES",
                # key="DATES_AS_STRINGS", # this does not work !
                freq="Q"
            )
        )
        .agg(
            FLOW_MEAN = ("FLOW", "mean"),
            FLOW_SUM = ("FLOW", "sum"),
            FLOW_MEDIAN = ("FLOW", "median")
        )
        .reset_index()
    )
    print(grouped, end="\n\n")










    # d = date.today()
    # s = d.strftime(FMT)
    # print(d, type(d), getsizeof(d), end="\n\n")
    # print(s, type(s), getsizeof(s), end="\n\n")



if __name__ == "__main__":
    main()
    pandas_example()
