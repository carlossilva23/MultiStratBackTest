"""
File: strategies.py
Purpose: This file will apply all strategies to each asset.
"""

def buyAndHold(asset):
    beg = asset.iloc[0]
    begP = beg["Close"]
    end = asset.iloc[-1]
    endP = end.iloc["Close"]

    totalReturn = (endP - begP) / begP
    return totalReturn