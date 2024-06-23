import ccxt
import pandas as pd
import ta

exchange = ccxt.bybit()

# Function to fetch K-line data
def fetch_klines(symbol, timeframe):
    klines = exchange.fetch_ohlcv(symbol, timeframe=timeframe)
    # Converts the data into a pandas DataFrame, to make it easier to handle. 
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    # Converts the timestamp from milliseconds to a datetime format for readability.
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Function to calculate RSI
def calculate_rsi(data, window):
    data['rsi'] = ta.momentum.RSIIndicator(data['close'], window=window).rsi()
    return data