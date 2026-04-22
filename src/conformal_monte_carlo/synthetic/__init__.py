"""Time series utilities package.

This package contains utility functions and classes for time series forecasting.
"""

from .dummy_predictor import DummyPredictor
from .dummy_ts_creator import create_dummy_ts

__all__ = [
    "DummyPredictor",
    "create_dummy_ts",
]