#!/usr/bin/env python3
import sys


def get_stock_info(company_or_ticker_key):
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

    if COMPANIES.get(company_or_ticker_key.capitalize()):
        print(f"{company_or_ticker_key.capitalize()} stock price is {STOCKS[COMPANIES[company_or_ticker_key.capitalize()]]}")
    elif STOCKS.get(company_or_ticker_key.upper()):
        tickers = {value: key for key, value in COMPANIES.items()}
        print(f"{company_or_ticker_key.upper()} is a ticker symbol for {tickers[company_or_ticker_key.upper()]}")
    else:
        print(f"{company_or_ticker_key} is an unknown company or an unknown ticker symbol")


def split_string(text):
    if text.count(",,"):
        return
    while text.count(", ") or text.count(" ,"):
        text = text.replace(", ", ",")
        text = text.replace(" ,", ",")
        if text.count(",,"):
            return

    text_list = text.split(",")
    for key in text_list:
        if key:
            get_stock_info(key.strip(" "))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        split_string(sys.argv[1])
