# pip3 install bs4
# pip3 install lxml

# https://yandex.com.am/weather/

import requests
from bs4 import BeautifulSoup


url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'

response = requests.get(url)
print(response)

soup = BeautifulSoup(response.text, "lxml")

# print(soup.prettify())

# temp = soup.find('span', 'temp__value temp__value_with-unit')
# print(temp.text)


temp2 = soup.find('div', 'temp fact__temp fact__temp_size_s')
print(temp2.next.text)

sum = 0
count = 0

for tag in soup.find_all('div', 'temp forecast-briefly__temp forecast-briefly__temp_day'):
    raw = tag.find('span', 'temp__value temp__value_with-unit')
    value = int(raw.text.replace('−', '-'))
    sum += value
    count += 1

print(sum // count)

# temp__value temp__value_with-unit

# print(soup.select('li:nth-of-type(3)'))
