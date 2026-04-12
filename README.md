# Yearly Uncertainty Quantification from Monthly Forecasts

This repository implements a lightweight framework for generating **yearly uncertainty estimates** from **monthly forecasts**, combining:

- **Monte Carlo simulation**
- **Stationary bootstrap** for residual resampling
- **Anchoring to monthly prediction intervals** using **Adaptive Conformal Inference (ACI)**

The goal is to produce **coherent, distribution‑aware yearly prediction intervals** that respect both monthly uncertainty and temporal dependence.

---

## 📌 Overview

Most demand forecasting pipelines provide **monthly point forecasts** and **monthly prediction intervals**, but business planning often requires **yearly uncertainty**. This project bridges that gap by:

- Sampling monthly forecast distributions via Monte Carlo  
- Modeling temporal dependence using stationary bootstrap  
- Aggregating simulated monthly paths into yearly totals  
- Ensuring consistency with monthly ACI‑derived intervals  

The result is a **robust, simulation‑based uncertainty quantification (UQ) workflow** suitable for hierarchical or business‑critical forecasting.

---

## 🧠 Methodology

### 1. Monthly Forecast Inputs
- Monthly point forecasts  
- Monthly prediction intervals (e.g., 5th–95th) from **ACI**  
- Historical residuals for bootstrap resampling  

### 2. Residual Modeling
Residuals are resampled using **stationary bootstrap**, preserving autocorrelation and seasonal structure.

### 3. Monte Carlo Simulation
For each iteration:

- Sample residual paths  
- Apply them to monthly forecasts  
- Generate a full 12‑month trajectory  
- Aggregate to yearly totals  

Typical configuration: **20,000+ iterations** for stable tail estimates.

### 4. Yearly Distribution Construction
From the simulated yearly totals:

- Compute quantiles  
- Construct prediction intervals  
- Optionally compare against monthly‑level uncertainty for coherence and anchor back for monthly corresponding interval