from unittest import TestCase
import pytest
import requests
import json

from app.models import Stock


class StockTestClass(TestCase):

    def test_get_all_stocks_returns_all(self):
        stocks = get_all_stocks()


    # def test_get_stock_by_ticker_returns_correct_stock(self):
    #     pass

    # def test_invalid_stock_not_found(self):
    #     stock = get_stock_by_ticker("TSLA")
    #     assert stock == None


    # def test_save_stock_success(self):

    #     with open('test/test_data/stock_test.json') as f:
    #         stock_data = json.load(f)



    # def test_save_duplicate_stock_rejected(self):
    #     prices = [
    #         {
    #             "date": "2022-01-01",
    #             "value": 201
    #         },
    #         {
    #             "date": "2022-01-02",
    #             "value": 199
    #         },
    #         {
    #             "date": "2022-01-03",
    #             "value": 205
    #         },
    #         {
    #             "date": "2022-01-04",
    #             "value": 205
    #         },
    #         {
    #             "date": "2022-01-05",
    #             "value": 206
    #         }
    #     ]

    #     # create stock and convert to __dict__

    #     # with pytest.raises(Exception, match="MSFT already exists") as excp:
    #     #     save_stock(data_json)


    # def test_convert_currency_is_correct(self):

    #     response = requests.get("https://open.er-api.com/v6/latest/USD")
    #     response = response.json()
    #     rates = response['rates']
    #     exchange_rate =rates['GBP']
    #     stock_expected = get_stock_by_ticker("APPL")

    #     # lambda with value



    def tearDown(self):
        original_stocks = self.return_original_stocks()

        with open('db/stock_db.json','w') as json_file:
            json.dump(original_stocks,json_file,indent=4,separators= (',',': '))

    def return_original_stocks(self):
        return [
            {
                "name": "Global Logic",
                "ticker_symbol": "GL",
                "analyst": "warren.buffet",
                "prices": [
                    {
                        "date": "2023-01-01",
                        "value": 54
                    },
                    {
                        "date": "2023-01-02",
                        "value": 55
                    },
                    {
                        "date": "2023-01-03",
                        "value": 53
                    },
                    {
                        "date": "2023-01-04",
                        "value": 55
                    },
                    {
                        "date": "2023-01-05",
                        "value": 56
                    }
                ]
            },
            {
                "name": "Microsoft",
                "ticker_symbol": "MSFT",
                "analyst": "peter.lynch",
                "prices": [
                    {
                        "date": "2023-01-01",
                        "value": 201
                    },
                    {
                        "date": "2023-01-02",
                        "value": 199
                    },
                    {
                        "date": "2023-01-03",
                        "value": 205
                    },
                    {
                        "date": "2023-01-04",
                        "value": 205
                    },
                    {
                        "date": "2023-01-05",
                        "value": 206
                    }
                ]
            },
            {
                "name": "Apple",
                "ticker_symbol": "APPL",
                "analyst": "cathy.wood",
                "prices": [
                    {
                        "date": "2023-01-01",
                        "value": 250
                    },
                    {
                        "date": "2023-01-02",
                        "value": 260
                    },
                    {
                        "date": "2023-01-03",
                        "value": 255
                    },
                    {
                        "date": "2023-01-04",
                        "value": 251
                    },
                    {
                        "date": "2023-01-05",
                        "value": 245
                    }
                ]
            }
        ]
