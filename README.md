# Multiple Strategy Backtest

## 1. Overview
I'm building a backtest in order to connect coding concepts I've attained to financial concepts I want to attain. Using different strategies, I'll be comparing each based on its returns and understanding the market conditions needed in order to maximize the benefits of each, through various time windows. I don't want to beat the market, just understand how it works. 

## 2. Strategies
Baseline: Buy and Hold 
Our baseline for this project will be a buy and hold strategy in which we initally buy a certain amount of shares at the beginning of each time period and compare it to the returns gained at the end of each time period. This strategy has less risk than the others and because we will not be executing any trades or selling any shares, this strategy could be used as a means of comparison with the others.  

Strategy 1: Moving Average Crossover 
Our first strategy is a simple moving average that will calculate two rolling averages (short and long), in order to see any trends that are ocurring in the market. As these averages update daily, buy and sell signals will generate whenever these two lines cross, eliminating short volatility and trading it for a broader overview of how stocks are moving. 

Strategy 2: Momentum 
Our second strategy will be a momentum strategy that will take into account trends and capitalize on peaks and lows. 

Strategy 3: Mean Reversion 
Our third strategy is a mean reversion strategy that implies that any stock or share will eventually revert to its historical price, so it takes advantage of assets that are overvalued or undervalued in orer to capitalize on the eventual drop or rise back to its historical data. 

## 3. Data
We are going to be using the SPY EFT asset to start and then eventually implement more assets as this project continues. We will be collecting data using the yfinance package in python.
We will be collecting historical data from three time windows: 6 Months, 1 Year and 5 Years. 

## 4. Methodology
## 5. Evaluation Metrics
## 6. Results
## 7. Limitations
## 8. Project Setup
## 9. How to Run
## 10. Dependencies
## 11. References 
