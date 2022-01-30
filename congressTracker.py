from ast import AsyncFunctionDef
import os
import csv
from datetime import date
import robin_stocks.robinhood as rs
from decouple import config


def getTransaction(d1):
    with open("all_transactions.csv") as f:
        csv_reader = csv.reader(f, delimiter = ",")
        for row in csv_reader:
            #print("henlo")
            if row[8] == "Hon. Patrick Fallon": # and row[1] == d1:
                ticker = row[4]
                p_sf_sp = row[6]
                amount = row[7]
                print(ticker + " " + p_sf_sp + "  " + amount)
                if p_sf_sp == "purchase":
                    buyTicker(ticker, amount)
                elif p_sf_sp == "sale_full":
                    sellFullTicker(ticker)
                elif p_sf_sp == "sale_partial":
                    sellPartTicker(ticker, amount)
                else:
                  ValueError("Not purchase, sale full or sale partial")

                
def buyTicker(ticker, amount):
    p_cash = float(rs.profiles.load_account_profile("portfolio_cash"))
    curr_ticker_price = rs.get_latest_price(ticker)[0]
    if type(curr_ticker_price) == str:
        print(type(curr_ticker_price))
        curr_ticker_price = float(curr_ticker_price)
        if amount == "$1,000 - $15,000":
            if (p_cash > curr_ticker_price * 0.1):
                rs.order_buy_fractional_by_quantity(ticker, 0.1)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$1,001 - $15,000":
            if (p_cash > curr_ticker_price * 0.1):
                rs.order_buy_fractional_by_quantity(ticker, 0.1)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$15,001 - $50,000":
            if (p_cash > curr_ticker_price * 0.2):
                rs.order_buy_fractional_by_quantity(ticker, 0.2)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$50,001 - $100,000":
            if (p_cash > curr_ticker_price * 0.3):
                rs.order_buy_fractional_by_quantity(ticker, 0.3)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$100,001 - $250,000":
            if (p_cash > curr_ticker_price * 0.4):
                rs.order_buy_fractional_by_quantity(ticker, 0.4)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$250,001 - $500,000":
            if (p_cash > curr_ticker_price * 0.5):
                rs.order_buy_fractional_by_quantity(ticker, 0.5)
            else:
                ValueError("Not enough funds to buy")
        elif amount == "$500,001 - $1,000,000":
            if (p_cash > curr_ticker_price * 0.6):
                rs.order_buy_fractional_by_quantity(ticker, 0.6)
            else:
                ValueError("Not enough funds to buy")
        else:
            ValueError("Buy price is too damn high")


def sellFullTicker(ticker):
    my_quant = _getholdingDict(ticker, 1)
    print(my_quant)
    rs.order_sell_fractional_by_quantity(ticker, my_quant)


def sellPartTicker(ticker, amount):
    my_price = _getholdingDict(ticker, 2)
    curr_ticker_price = rs.get_latest_price(ticker)
    if amount == "$1,000 - $15,000":
        if (my_price > curr_ticker_price * 0.1):
            rs.order_sell_fractional_by_quantity(ticker, 0.1)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$1,001 - $15,000":
        if (my_price > curr_ticker_price * 0.1):
            rs.order_sell_fractional_by_quantity(ticker, 0.1)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$15,001 - $50,000":
        if (my_price > curr_ticker_price * 0.2):
            rs.order_sell_fractional_by_quantity(ticker, 0.2)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$50,001 - $100,000":
        if (my_price > curr_ticker_price * 0.3):
            rs.order_sell_fractional_by_quantity(ticker, 0.3)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$100,001 - $250,000":
        if (my_price > curr_ticker_price * 0.4):
            rs.order_sell_fractional_by_quantity(ticker, 0.4)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$250,001 - $500,000":
        if (my_price > curr_ticker_price * 0.5):
            rs.order_sell_fractional_by_quantity(ticker, 0.5)
        else:
            ValueError("Not enough funds to sell")
    elif amount == "$500,001 - $1,000,000":
        if (my_price > curr_ticker_price * 0.6):
            rs.order_sell_fractional_by_quantity(ticker, 0.6)
        else:
            ValueError("Not enough funds to sell")
    else:
        ValueError("Sell price is too damn high")



def _getholdingDict(ticker, choice):
    holdings_dict = rs.build_holdings()
    for key in holdings_dict:
        if key == ticker and choice == 1:
            return(holdings_dict[key]["quantity"])
        if key == ticker and choice == 2:
            return(holdings_dict[key]["price"])

if __name__ == "__main__":
    today = date.today()
    d1 = today.strftime("%m/%d/%Y")
    d1 = "7/2/2021"
    
    
    user = config("user", default="")
    password = config("password", default="")
    rs.login(user, password)
    getTransaction(d1)


