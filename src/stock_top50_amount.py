import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup

yahoo_top20_url = "https://tw.stock.yahoo.com/d/i/rank.php?t=vol&e=otc"


class StockTop50:
    def get_top20_stock(self, murl):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        tbls = soup.find_all("table")

        for tbl in tbls:
            rows = tbl.find_all("tr")
            for row in rows:
                cols = row.findAll("td")
                for col in cols:
                    if col.has_attr("class") and col["class"][0] == "name":
                        ns = col.findAll("a")
                        get_name(ns)

    def get_name(self, names):
        for n in names:
            data = n.getText().split(" ")
            stock_code = data[0]
            stock_name = data[1]
            print(f"stock code : {stock_code}, stock name:{stock_name}")


if __name__ == "__main__":
    top50 = StockTop50()
    get_top20_stock(yahoo_top20_url)
    pass
