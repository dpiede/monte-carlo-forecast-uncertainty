"""Module containing conformal predictor classes for time series forecasting."""

import pandas as pd
from darts import TimeSeries

class ConformalPredictorSCP:
    """A conformal predictor using the Split Conformal Prediction (SCP) method.
    
    Split Conformal Prediction is a distribution-free method that constructs
    prediction intervals with finite-sample coverage guarantees.
    """
    ...
    
class ConformalPredictorACI:
    """A conformal predictor using the Adaptive Conformal Inference (ACI) method.
    
    Adaptive Conformal Inference dynamically adjusts prediction intervals based
    on recent coverage performance.
    """
    ...
    
class ConformalPredictorPooledConformal:
    """A conformal predictor using the Pooled Conformal method.
    
    Pooled Conformal Prediction uses a pool of historical residuals to construct
    prediction intervals.
    """
    ...