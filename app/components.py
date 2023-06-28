import json

import requests

from app.models import Stock

def get_all_stocks():

    with open('project/tdd_stock/db/stock_db.json') as dbfile:
        stocks_json = json.load(dbfile)



def get_stock_by_ticker(ticker_symbol):
    with open('project/tdd_stock/db/stock_db.json') as dbfile:
        stocks_json = json.load(dbfile)

    

# def save_stock(stock_to_save):
        #     with open('db/stock_db.json','r') as json_db:
#         stock_list = json.load(json_db)
#     # stock_list_obj = list(map(lambda x:Stock(**x), stock_list))
#     # stock_obj = Stock(**stock_to_save)
#     # stock_list_obj.append(stock_obj)

#     stock_list_json = list(map(lambda x: vars(x), stock_list_obj))
#     with open('db/stock_db.json','w') as json_db:
#         json.dump(stock_list_json,json_db,sort_keys=True, indent=4, separators=(',', ': '))
#     # else:
#     #     raise Exception(f"{stock_obj.ticker_symbol} already exists")
            
# def load_db():
#     with open('db/stock_db.json','r') as json_db:
#         stock_list = json.load(json_db)
#     return stock_list

    

# def get_stock_with_conversion(ticker_symbol,conversion):

#     response = requests.get("https://open.er-api.com/v6/latest/USD")
#     response = response.json()
#     rates = response['rates']
#     exchange_rate =rates[conversion]

#     stock = get_stock_by_ticker(ticker_symbol)

#     converted_prices = list(map(lambda x:x["value"]* exchange_rate,stock.prices))
#     stock.prices = converted_prices
    







