### This module contains a predictor using XGBoost, to predict on the dummy dataset.

import pandas as pd
from darts import TimeSeries
from darts.models import XGBModel

class DummyPredictor:
    def __init__(self):
        self.model = XGBModel()
        
    def fit(self, series: TimeSeries):
        ...