import pandas as pd
    
def simulate_portfolio(ticker_data): 
    pv_history = []
    trade_log = []
    cash = 11000
    holdings = {}
    for ticker in ticker_data.keys(): 
        holdings[ticker] = 0

    control = next(iter(ticker_data.values()))
    dates = control.index

    for date in dates: 
        for symbol, ticker in ticker_data.items(): 
            ticker = ticker.sort_index()
            ticker = ticker[~ticker.index.duplicated(keep='first')]
            buy_signal = ticker.loc[date, 'Buy Signal']
            buy_signal = buy_signal.item()
            sell_signal = ticker.loc[date, 'Sell Signal']
            sell_signal = sell_signal.item()
            price = ticker.loc[date, 'Close']
            price = price.item()
            if (sell_signal == True) and (holdings[symbol] > 0):
                shares = holdings[symbol]
                cash += (shares * price)
                holdings[symbol] = 0
                log_trade(trade_log, date, symbol, "Sell", price, shares, cash, holdings, ticker_data)
            elif (buy_signal == True) and (cash > 1000):
                shares = 1000 // price
                holdings[symbol] = shares
                remaining = 1000 - (shares * price)
                cash = (cash - 1000) + remaining 
                log_trade(trade_log, date, symbol, "Buy", price, shares, cash, holdings, ticker_data)
        pv_history.append((date, cash + sum(holdings[symbol] * price)))

    return (pd.DataFrame(trade_log), 
            pd.DataFrame(pv_history, columns =['Date', 'Portfolio Value']))
            
        
                
def log_trade(trade_log, date, symbol, action, price, shares, cash, holdings, ticker_data):
    total_holdings = 0
    for stock, holds in holdings.items(): 
        total_holdings += holds
    trade_pv = cash + sum(holdings[stock] * ticker_data[stock].loc[date, "Close"])
    trade_log.append({
        "Date": date,
        "Ticker": symbol,
        "Action": action,
        "Price": price,
        "Shares": shares,
        "Cash": cash,
        "Holdings": total_holdings,
        "Portfolio Value": trade_pv,
    })
    
