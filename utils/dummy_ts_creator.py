"""Module for creating dummy time series datasets for testing."""

import pandas as pd
from sktime import datasets


def create_dummy_ts() -> pd.DataFrame:
    """Creates a dummy time series dataset using sktime's hierarchical data.
    
    For rows with product line 'Food preparation' and product group 'Hobs':
    - Changes the product line to 'Food preservation' and product group to 'Dehydrators'
    - Removes the first 48 of these rows
    
    Returns:
        A DataFrame containing the modified time series data.
    """
    df = datasets.load_hierarchical_sales_toydata().reset_index()
    
    mask = (df["Product line"] == "Food preparation") & (df["Product group"] == "Hobs")
    df.loc[mask, ["Product line", "Product group"]] = ["Food preservation", "Dehydrators"]
    df = df.drop(df[mask].index[:48]).reset_index(drop=True)
    
    return df