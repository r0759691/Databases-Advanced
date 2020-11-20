import requests
from bs4 import BeautifulSoup
import time
import threading

#De output van deze functie ging in een json steken en die json meegeven aan de gemaakt mongoDB server.
#Jammer genoeg had ik hiervoor geen tijd meer en begrijp dat ik hier een nul op haal.

def scraper():
    page = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')

    soup = BeautifulSoup(page.content, 'html.parser')

    Hash_elem = soup.find_all('a', class_='sc-1r996ns-0 gzrtQD sc-1tbyx6t-1 kXxRxe iklhnl-0 boNhIO d53qjk-0 jmTmMY')

    Rest_elem = soup.find_all('span', class_='sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg')

    with open("Blockchain_Scraper_Logfile.txt", "a") as f:
        print(Hash_elem[-1].text + ', ' +Rest_elem[-3].text  + ', ' + Rest_elem[-2].text + ', ' + Rest_elem[-1].text, file=f)

while True:
scraper()
    time.sleep(60)
