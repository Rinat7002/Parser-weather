from bs4 import BeautifulSoup
import requests

url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A3%D1%84%D0%B5"
response = requests.get(url)
bs = BeautifulSoup(response.text,"html.parser")

temp = bs.find('span', 't_0')

print(temp.text)
