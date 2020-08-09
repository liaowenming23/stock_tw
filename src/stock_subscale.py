import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup

url = "https://tw.stock.yahoo.com/q/ts?s={}"


class StockSubscale:
    def get_subscale(self, stock_code):
        response = requests.get(url.format(stock_code))
        soup = BeautifulSoup(response.text, "lxml")

        tabl = soup.find("table", {"style": "border-collapse=collapse;"})
        get_all_price_amount(tabl)

    def get_all_price_amount(self, tabl):
        records = tabl.find_all("table")
        for record in records:
            tds = record.find_all("td")
            print(f"price:{tds[0].getText()}, amout:{tds[2].getText()}")


if __name__ == "__main__":
    subscale = StockSubscale()
    subscale.get_subscale("9958")
    pass
