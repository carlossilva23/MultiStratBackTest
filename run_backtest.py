import clean_data
import strategies
import evaluate

def main(): 
    ticker = "SPY"
    period_date = "1y"
    data = clean_data.download_data(ticker, period_date)
    apply_base = strategies.baseline(data)
    metrics = evaluate.apply_metrics(data, apply_base)
    print(metrics)
main()
