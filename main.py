import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://netstalkers.com")
soup = BeautifulSoup(response.text, "lxml")

print(soup.find("h1").text)
