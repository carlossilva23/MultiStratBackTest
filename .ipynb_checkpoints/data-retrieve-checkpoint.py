import yfinance as yf

asset = yf.download("SPY", period="6mo")
clean_asset = asset["Close"].dropna()

