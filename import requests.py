import requests
from bs4 import BeautifulSoup

# ウェブページのURLを指定
url = "https://finance.yahoo.co.jp/quote/998407.O"

# requestsを使用してウェブページを取得
response = requests.get(url)

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(response.content, "html.parser")

# ウェブページのタイトルを取得
title = soup.title.string

print(title)

