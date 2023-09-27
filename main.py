import requests
from bs4 import BeautifulSoup

location_id = 355579
url = "https://api.openaq.org/v2/locations/{location_id}"
#url = https://api.openaq.org/v2/measurements?location_id=355579&parameter=um025&parameter=pm10&parameter=um100&parameter=um050&parameter=um003&parameter=pressure&parameter=temperature&parameter=humidity&parameter=um005&parameter=um010&parameter=pm1&parameter=pm25&date_from=2023-09-25T14:05:17-04:00&date_to=2023-09-26T14:05:17-04:00&limit=1000
res = requests.get(url)
data = res.json()
header = {"Accept": "application/json"}
response = requests.get(url, headers=header)
print(response.json())


def getdata(url):
  r= requests.get(url)
  return r.text

htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')
#result = soup.find_all(class = )
                   
  


