"""Module for creating dummy time series datasets for testing."""

import pandas as pd
from sktime import datasets
from darts import TimeSeries


def create_dummy_ts() -> tuple[pd.DataFrame, list[TimeSeries]]:
    """Creates a dummy time series dataset using sktime's hierarchical data.
    
    For rows with product line 'Food preparation' and product group 'Hobs':
    - Changes the product line to 'Food preservation' and product group to 'Dehydrators'
    - Removes the first 48 of these rows
    
    Returns:
        A DataFrame containing the modified time series data and a list of TimeSeries objects.
    """
    df = datasets.load_hierarchical_sales_toydata().reset_index()
    
    mask = (df["Product line"] == "Food preparation") & (df["Product group"] == "Hobs")
    df.loc[mask, ["Product line", "Product group"]] = ["Food preservation", "Dehydrators"]
    df = df.drop(df[mask].index[:48]).reset_index(drop=True)
    df["Date"] = df["Date"].dt.to_timestamp()
    ts_list = TimeSeries.from_group_dataframe(df, group_cols=["Product line", "Product group"], time_col="Date", value_cols="Sales")
    
    return df, ts_list