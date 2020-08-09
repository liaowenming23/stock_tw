import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup

url = "https://goodinfo.tw/StockInfo/ShowBuySaleChart.asp?STOCK_ID={}&CHT_CAT=DATE"
headers = {
    "User-Agent":  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}


class StockInstituInvestros:
    def get_buy_sale_detail_data(self, stock_code):
        response = requests.get(url.format(stock_code), headers=headers)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "lxml")
        tr = soup.find("tr", {"id": "row0"})
        tds = tr.find_all("td")
        print(f"foreign investors buy:{tds[5].getText()}")
        print(f"foreign investors sale:{tds[6].getText()}")
        print(f"investment trust buy:{tds[10].getText()}")
        print(f"investment trust sale:{tds[11].getText()}")
        print(f"dealer buy:{tds[13].getText()}")
        print(f"dealer sale:{tds[14].getText()}")


if __name__ == "__main__":
    investors = StockInstituInvestros()
    investors.get_buy_sale_detail_data("9958")
    pass
