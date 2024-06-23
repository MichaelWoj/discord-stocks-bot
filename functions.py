import ccxt
import pandas as pd
import ta

exchange = ccxt.bybit()

def fetch_klines(symbol, timeframe):
    klines = exchange.fetch_ohlcv(symbol, timeframe=timeframe)
    # Converts the data into a pandas DataFrame, to make it easier to handle. 
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # Converts the timestamp from milliseconds to a datetime format for readability.
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_rsi(data, window):
    # Uses the Technical Analysis library to calculate the RSI over a specified time window 
    data['rsi'] = ta.momentum.RSIIndicator(data['close'], window=window).rsi()
    return data