import requests
from bs4 import BeautifulSoup

url = "https://api.openaq.org/v2/locations?parameters=pm25"

def getdata(url):
  r= requests.get(url)
  return r.text


