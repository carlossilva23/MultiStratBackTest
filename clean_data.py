import yfinance as yf
import matplotlib.pyplot as plt

# Download Data and Create Daily Return Column
def download_data(ticker, period_date):
    asset = yf.download(ticker, period= period_date)
    clean_asset = asset["Close"].dropna()
    clean_asset["Daily Return"] = (clean_asset[ticker].pct_change().dropna()) * 100
    clean_asset.iloc[0, 1] = 0

    # Plot Asset Price 
    plt.figure(figsize=(10,10))
    plt.plot(clean_asset[ticker], label='Closing Price', color='blue')
    plt.title(f"{ticker} Historical Data")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.show()

    return clean_asset



