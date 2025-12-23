import pandas as pd
import matplotlib.pyplot as plt

def apply_metrics(data, pos_series): 
    # Calculate Strategy Return 
    strat_return = pd.Series(index = pos_series.index)
    strat_return = pos_series.shift(1) * data["Daily Return"]
    strat_return.iloc[0] = 0

    # Calculate Equity
    equity_series = pd.Series(index = pos_series.index)
    equity_series.iloc[0] = 1.0
    equity_series = (1 + strat_return).cumprod()

    # Create Basic Metric Table (df)
    eval_df = {
        "Baseline": [0, 0, 0, 0, 0], 
        "Moving Average": [0, 0, 0, 0, 0], 
        "Momentum": [0, 0, 0, 0, 0],
        "Mean Reversion": [0, 0, 0, 0, 0]
    }

