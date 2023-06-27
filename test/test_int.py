import json
from app.app import app
from app.models import Stock


class TestClass:

    @classmethod
    def setup_method(self):
        app.config["TESTING"] = True

        with app.test_client() as client:
            self.client = client

    # @classmethod
    # def teardown_method(self):
    #     original_stocks = self.return_original_stocks(self)

    #     with open('db/stock_db.json','w') as json_file:
    #         json.dump(original_stocks,json_file,indent=4,separators= (',',': '))

    
    def test_get_all_stocks(self):
        response = self.client.get("/stock/all_stocks/")

        assert response.status_code == 200


    def test_get_stock_by_ticker_integration(self):

        response = self.client.get(
            f"/stock/APPL/",
            content_type="application/json"
        )

        # json_response = response.json
        # stock = Stock(**json_response)
        # assert stock.ticker_symbol == 'APPL'


    # def test_add_stock_integration(self):

    #     with open('test/test_data/stock_test.json') as f:
    #         stock_data = json.load(f)

    #     data_json = json.dumps(stock_data)


    # def test_add_stock_duplicate_rejected(self):

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

    #     stock =  Stock("dave","Microsoft","MSFT",prices)
    #     data_json = stock.__dict__
        
    #     data_json = json.dumps(data_json)
    #     response = self.client.post(
    #         "/add-stock/",
    #         data = data_json,
    #         content_type = "application/json"
    #     )




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