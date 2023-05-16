import pandas as pd

# 이동 평균선
def ma(source, length):     
    return source.rolling(window=length).mean()


# 최대 최소값
def max(source, length):
    return source.rolling(window=length).max()

def min(source, length):
    return source.rolling(window=length).min()


# rsi 미완성
# def rsi(source, length):
#     sourceu = source
#     sourced = source
    
#     for i in range(0, -length, -1):
#         if source[i] > source.shift(-1):
#             sourceu.append(source - source.shift(-1).fillna(0))
#         elif source[i] <= source[i-1]:
#             sourced.append(source.shift(-1).fillna(0) - source)
    
#     print(sourceu)
#     au = sum(u)/len(u)
#     ad = sum(d)/len(d)
#     rs = au/ad
    
#     return rs / (rs + 1) * 100


# 스토캐스틱
def fstochastic(source, length):  
    top = source['close'] - source['low'].rolling(window=length).min()
    bot = source['high'].rolling(window=length).max() - source['low'].rolling(window=length).min()
    K = top / bot* 100
    return K

def fstochastic(close, high, low, length):  
    top = close - low.rolling(window=length).min()
    bot = high.rolling(window=length).max() - low.rolling(window=length).min()
    K = top / bot* 100
    return K









"""
MIT License

Copyright (c) 2023 ZaRi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  
"""