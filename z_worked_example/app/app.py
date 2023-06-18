from flask import Flask, Response, app, jsonify, request
from app.components import get_all_stocks, get_stock_by_ticker, get_stock_with_conversion, save_stock
from app.models import Stock

app = Flask(__name__)


@app.route("/stock/<ticker_symbol>/",methods=["GET"])
def get_stock_by_ticker_symbol(ticker_symbol):
    stock = get_stock_by_ticker(ticker_symbol)
    if stock:
        return jsonify(stock.__dict__)
    else:
        return jsonify(None)


@app.route("/stock/conversion/<ticker_symbol>/<conversion>", methods=["GET"])
def get_stock_by_conversion(ticker_symbol,conversion):
    stock = get_stock_with_conversion(ticker_symbol)
    if stock:
        return jsonify(stock.__dict__)
    else:
        return jsonify(None)

@app.route("/stock/all_stocks/", methods=["GET"])
def get_all():
    stocks = get_all_stocks()
    return jsonify([vars(e) for e in stocks])

@app.route("/add-stock/",methods=["POST"])
def add_stock_to_db():
    # try catch for error
    try:
        stock_input = Stock(**request.json)
        save_stock(stock_input)
        resp = jsonify(success=True)
        return resp
    except Exception as e:
        return Response(f'{str(e)}',status=400)