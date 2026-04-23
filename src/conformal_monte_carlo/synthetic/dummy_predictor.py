"""Module for dummy prediction using XGBoost on test datasets.

This module contains a predictor class for making predictions on time series
data using XGBoost, intended for testing purposes.
"""

import pandas as pd
from darts import TimeSeries
from darts.utils.timeseries_generation import datetime_attribute_timeseries
from darts.models import XGBModel
from typing import Any

class DummyPredictor:
    """A dummy predictor using XGBoost for testing purposes."""
    
    def __init__(self, series: TimeSeries, n: int = 24):
        """Initializes the DummyPredictor and runs predictions.
        
        Args:
            series: A TimeSeries object to fit and predict on.
            n: Number of steps ahead to predict. Defaults to 24.
        """
        self.series = series
        self.n = n
        self.train, self.test = self.train_test_split()
        self.future_covariates = datetime_attribute_timeseries(self.train, "month", cyclic = True, add_length = self.n)
        self.model = XGBModel(
            lags = 12, 
            lags_future_covariates = [l for l in range(self.n)], 
            output_chunk_length = self.n,
            use_static_covariates = False,
            )
        
    def train_test_split(self) -> tuple[TimeSeries, TimeSeries]:
        """Splits the time series into training and testing sets.
        
        Uses the `n` attribute to determine the test set size (last n steps).
        
        Returns:
            A tuple containing the training and testing time series.
        """
        self.train, self.test = self.series[:-self.n], self.series[-self.n:]
        return self.train, self.test
        
    def fit(self) -> None:
        """Fits the XGBoost model to the time series data."""
        self.model.fit(self.train, future_covariates=self.future_covariates)
    
    def predict(self):
        """Generates predictions for n steps ahead.
        
        Returns:
            A TimeSeriesLike object containing the predictions.
        """
        predictions = self.model.predict(self.n, future_covariates=self.future_covariates)
        return predictions
    
    def run(self) -> tuple[Any, TimeSeries, TimeSeries]:
        """Fits the model and generates predictions.
        
        Returns:
            A tuple containing the predictions, training set, and test set.
        """
        self.fit()
        return self.predict(), self.train, self.test