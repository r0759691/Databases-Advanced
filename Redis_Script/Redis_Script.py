import requests
from bs4 import BeautifulSoup
import time
import threading
import redis
import json

r = redis.Redis()
#col_DaDbBits = "DaDbBits"
#r.sadd(col_DaDbBits, "Most_valuable_hash")

def scraper():
    page = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')

    soup = BeautifulSoup(page.content, 'html.parser')

    Hash_elem = soup.select("a.sc-1r996ns-0.fLwyDF.sc-1tbyx6t-1.kCGMTY.iklhnl-0.eEewhk.d53qjk-0.ctEFcK")

    Rest_elem = soup.select("span.sc-1ryi78w-0.cILyoi.sc-16b9dsl-1.ZwupP.u3ufsr-0.eQTRKC")

    content = []
    for i in range(len(Hash_elem)):
        line = []
        line.append(Hash_elem[i].text)
        line.append(Rest_elem[i*3].text)
        line.append(float(Rest_elem[i*3+1].text.replace(" BTC", "")))
        line.append(Rest_elem[i*3+2].text)
        content.append(line)
  
    content.sort(key=lambda x:x[2])
    Redis_json = {"Hash": content[-1][0], "Time": content[-1][1], "BTC": str(content[-1][2]), "Dollars": content[-1][3]}
    json_dump = json.dumps(Redis_json)
    r.set("Hash", json_dump, ex=60)
    r.get("Hash")
    print(Redis_json)

while True:
    scraper()
    time.sleep(60)