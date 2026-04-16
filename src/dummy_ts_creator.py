import pandas as pd
from sktime import datasets

def create_dummy_ts():
    df = datasets.load_hierarchical_sales_toydata().reset_index()
    return df