# Retail Sales Forecasting

## Project Overview
Forecast weekly sales for multiple products across stores to optimize inventory, supply chain, and staffing.

## Dataset
Historical sales data with columns like `date`, `store_nbr`, `family`, `sales`, `onpromotion`, and external features like holidays and oil price (`dcoilwtico`). Preprocessed and feature-engineered dataset saved as `merged_feature_engineered.parquet`.

## Preprocessing & Feature Engineering
- Handled missing values.  
- Encoded categorical features: `store_nbr`, `family`, `city`, `state`, `type`, `cluster`.  
- Created time-based features: `day_of_week`, `month`, `year`, `week_of_year`, `is_holiday`.  
- Added lag features: `sales_last_week`, `sales_two_weeks_ago`.  
- Added rolling averages: `rolling_4_weeks`, `rolling_8_weeks`.

## Modeling
- **Baseline:** ARIMA (captures temporal patterns).  
- **Advanced:** XGBoost and LightGBM (regression models using engineered features).

## Evaluation Metrics
- **MAE:** Average absolute error between predicted and actual sales.  
- **RMSE:** Penalizes large errors, important for retail forecasting.  

| Model      | MAE   | RMSE  |
|----------- |------ |------ |
| ARIMA      | 9.50  | 11.35 |
| XGBoost    | 3.75  | 27.78 |
| LightGBM   | 2.19  | 21.21 |

## Key Takeaways
- LightGBM gives the best performance.  
- Time-based, lag, and rolling features capture seasonality effectively.  
- Categorical features help generalize patterns across stores and products.

## Saved Models
- `arima_model.pkl`  
- `xgboost_model.pkl`  
- `lightgbm_model.pkl`

## Forecasting & Result Generation

Used the trained LightGBM model to forecast next week’s sales for all store-family combinations.

Ensured all negative predictions were clipped to 0.

Forecast results saved as CSV (weekly_forecast_YYYY-MM-DD.csv) for submission and further analysis.

