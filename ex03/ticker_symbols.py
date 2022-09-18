#!/usr/bin/env python3
import sys


def get_stock_price(ticker_name):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }

    if (STOCKS.get(ticker_name)) and (ticker_name in COMPANIES.values()):
        tickers = {value: key for key, value in COMPANIES.items()}
        return f"{tickers[ticker_name]} {STOCKS[ticker_name]}"
    return "Unknown ticker"


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_stock_price(sys.argv[1].upper()))
