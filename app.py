import pandas as pd
import yfinance as yf
import ta

nifty_500_symbols = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"
    # Aap full list baad me daal sakte ho
]

def fetch_data(symbol, interval="1d", period="60d"):
    data = yf.download(symbol, interval=interval, period=period)
    data.dropna(inplace=True)
    data['20EMA'] = ta.trend.ema_indicator(data['Close'], window=20).ema_indicator()
    data['30SMA'] = ta.trend.sma_indicator(data['Close'], window=30).sma_indicator()
    data['200EMA'] = ta.trend.ema_indicator(data['Close'], window=200).ema_indicator()
    return data

def scan_stocks():
    result = []
    for symbol in nifty_500_symbols:
        try:
            df = fetch_data(symbol)
            latest = df.iloc[-1]
            if (
                latest['Close'] > latest['20EMA'] > latest['30SMA'] > latest['200EMA']
            ):
                result.append(symbol)
        except Exception as e:
            print(f"Error for {symbol}: {e}")
    return result

if __name__ == "__main__":
    stocks = scan_stocks()
    print("Filtered stocks based on EMA/SMA strategy:")
    for s in stocks:
        print(s)
