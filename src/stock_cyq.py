import requests
import lxml
import pandas as pd
from bs4 import BeautifulSoup

url = "https://concords.moneydj.com/z/zc/zcj/zcj_{}.djhtm"

cyq_name = ["director", "foreign investors", "investment trust buy","dealer buy", "margin trading", "selling short"]

class StockCYQ:
    def get_cyq(self, stock_code):
        response = requests.get(url.format(stock_code))
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find("table", {"class": "t01"})

        trs = data.find_all("tr")
        for i in range(2, 8):
            tds = trs[i].find_all("td")
            print(f"{cyq_name[i-2]}: {tds[1].getText()}, {tds[3].getText()}")
            


if __name__ == "__main__":
    stock_cyq = StockCYQ()
    stock_cyq.get_cyq("9958")
    pass
