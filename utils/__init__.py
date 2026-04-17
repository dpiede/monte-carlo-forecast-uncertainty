"""Utils package.

This package contains utility functions and classes for the project.
"""

from .dummy_predictor import DummyPredictor
from .dummy_ts_creator import create_dummy_ts

__all__ = [
    "DummyPredictor",
    "create_dummy_ts",
]