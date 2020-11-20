import requests
import re
from bs4 import BeautifulSoup
import time
import threading

#def scraper():
MoneyList = []

page = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')

soup = BeautifulSoup(page.content, 'html.parser')

Hash_elem = soup.find_all('a', class_='sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO d53qjk-0 jmTmMY')

Rest_elem = soup.find_all('span', class_='sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg')

#print(Rest_elem[2])

i = 2
while i != 149:
    MoneyList.append(Rest_elem[i].text)
    i+=3

#print(MoneyList[0])

NewList = []
k = 0
while k != len(MoneyList):
    getal = MoneyList[k][1:].replace(',','')
    NewList.append(getal)
    k+=1

#print(NieuweList[0])

#In het deel hieronder zat ik vast want the types van de variabelen klopten niet.
#Als ze klopten ging ik het grootste getal terugvinden in Rest_elem en dan daaruit de meest kostbare hash eruit halen
j = 0
GrootsteGetal = 0.0
while j != len(NewList):
    if float(NewList[j]) > GrootsteGetal:
        GrootsteGetal = float(NewList[j])
    j+=1

hash_index = Rest_elem.index(GrootsteGetal) // 3
index_time = Rest_elem.index(GrootsteGetal) - 2
index_BTC = Rest_elem.index(GrootsteGetal) - 1
index_bedrag = Rest_elem.index(GrootsteGetal)

with open("Blockchain_Scraper_Logfile.txt", "a") as f:
    print(Hash_elem[hash_index].text + ', ' +Rest_elem[index_time].text  + ', ' + Rest_elem[index_BTC].text + ', ' + Rest_elem[index_bedrag].text, file=f)

#while True:
#    scraper()
#    time.sleep(60)