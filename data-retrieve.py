"""
File: data-retrieve.py
Purpose: This file will clean any dataframe needed
and will send it to the rest of the project. 
"""
import yfinance as yf

asset = yf.download("SPY", period="6mo")
clean_asset = asset["Close"].dropna()
clean_asset["Daily Return"] = (clean_asset["SPY"].pct_change().dropna()) * 100

