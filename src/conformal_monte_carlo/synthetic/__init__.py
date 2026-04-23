"""Time series utilities package.

This package contains utility functions and classes for time series forecasting.
"""

from .dummy_predictor import DummyPredictor
from .dummy_ts_generator import generate_dummy_ts
from .synthetic_data_generator import SyntheticDataGenerator

__all__ = [
    "DummyPredictor",
    "generate_dummy_ts",
    "SyntheticDataGenerator",
]