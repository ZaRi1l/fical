import pandas as pd
import ccxt
import mplfinance as mpf

symbol = 'BTC/USDT'
timeframe = '1h'
candle = 100

binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv(symbol, timeframe = timeframe, limit = candle)
# timeframe
# 1m 1분
# 1h 1시간
# 1d 하루

# limit
# 봉 개수

df = pd.DataFrame(btc_ohlcv, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
df['date'] = pd.to_datetime(df['date'], unit='ms')
df = df.set_index('date')

df_t = df.tail(100)  # 최근 10개의 캔들 가져오기
print(df_t)
mpf.plot(df_t, type='candle')