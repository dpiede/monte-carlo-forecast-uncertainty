"""Generates synthetic data for testing the conformal Monte Carlo method.

The generated data can be used to test the the conformal Monte Carlo
method in estimating prediction intervals and quantiles.
"""

from . import dummy_ts_generator as dtg
from . import dummy_predictor as ddp
import numpy as np

class SyntheticDataGenerator:
    """Generates synthetic data for testing the conformal Monte Carlo method."""

    def __init__(self):
        """Initializes the SyntheticDataGenerator.
        
        Loads dummy time series data and prepares the data generation pipeline.
        """
        self.df, self.ts_list = dtg.generate_dummy_ts()
        self.pred_ts_dict = {}
        self.train_ts_dict = {}
        self.test_ts_dict = {}

    def generate_predictions(self, n: int = 24) -> tuple[dict, dict, dict]:
        """Generates synthetic predictions for time series.
        
        Args:
            n: Number of steps ahead to predict. Defaults to 24.
            
        Returns:
            A tuple of three dictionaries: predictions, training sets, and test sets.
        """
        for ts in self.ts_list:
            pred_ts_i, train_ts_i, test_ts_i = ddp.DummyPredictor(ts, n).run()
            cov_values = ts.static_covariates_values()
            
            if cov_values is not None:
                key = tuple(cov_values.flatten())
            else: 
                continue
        
            self.pred_ts_dict[key] = pred_ts_i
            self.train_ts_dict[key] = train_ts_i
            self.test_ts_dict[key] = test_ts_i
        return self.pred_ts_dict, self.train_ts_dict, self.test_ts_dict




