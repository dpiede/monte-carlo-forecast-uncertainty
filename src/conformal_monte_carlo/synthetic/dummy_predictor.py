### This module contains a predictor using XGBoost, to predict on the dummy dataset.

import pandas as pd
from darts import TimeSeries
from darts.models import XGBModel

class DummyPredictor:
    """A dummy predictor using XGBoost for testing purposes."""
    def __init__(self):
        self.model = XGBModel()
        
    def fit(self, series: TimeSeries):
        self.model.fit(series)
    
    def predict(self, n: int) -> TimeSeries:
        predictions = self.model.predict(n)
        return predictions # type: ignore