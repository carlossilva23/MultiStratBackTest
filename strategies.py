import pandas as pd

def baseline(data): 

    # Create Baseline Pos Series
    dates = data.index
    baseline_series = pd.Series(1, index=dates)

    return baseline_series



