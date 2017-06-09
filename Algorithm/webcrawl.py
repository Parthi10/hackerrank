import requests  as req
from bs4 import BeautifulSoup as BS

#proxy = {'http': 'http://069.15084015:rishu3229@10.1.1.45:80'}

url = "http://10.8.0.1/main.html"

source_code = req.get(url)
plain_text = source_code.text
soup = BS(plain_text,"html.parser")
print(soup)
