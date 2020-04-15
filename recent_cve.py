from pymongo import MongoClient
import requests
import json
import urllib3
from bs4 import BeautifulSoup
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb://root:password@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.find_my_cve
#Step 2: Récupérer le flux des dernières CVE
last_cve = requests.get("http://www.cvedetails.com/json-feed.php?numrows=10&vendor_id=0&product_id=0&version_id=0&hasexp=1&opec=1&opov=1&opcsrf=1&opfileinc=1&opgpriv=1&opsqli=1&opxss=1&opdirt=1&opmemc=1&ophttprs=1&opbyp=1&opginf=1&opdos=1&orderby=2&cvssscoremin=0")
curl = last_cve.text
jsondatas = json.loads(curl)
print(jsondatas[2])
#Step 3: on boucle sur les dernières CVE pour accéder à chacun de leurs urls, et récupérer le reste des données
for json_data in jsondatas:
    print(json_data['url'])
    url=json_data['url']
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    #Step 4 : on parse la page html pour obtenir le tableau des données (CVE Score, etc.)
    soup = BeautifulSoup(response.data.decode('utf-8'), "html.parser")
    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="cvssscorestable")
    #Step 5 : on enlève les données qui sont en double par rapport au premier appel de l'API
    soup.find('th', string="CVSS Score").decompose() 
    soup.find('th', string="CWE ID").decompose()   
    keys = [th.get_text(strip=True)for th in table.find_all('th')]
    values = [td.get_text(strip=True) for td in table.find_all('td')]
    k=[]
    for i in keys :
        j = i.replace(' ','_').replace('(', '').replace(')', '')
        k.append(j)
    #Step 6 : on regroupe les données dans un seul et même dictionnaire, qu'on push ensuite dans la DB Mongo
    d = dict(zip(k, values))
    #initiliaze a variable
    convert_to_uppercase = {k.lower(): v for k, v in d.items()}
    print(d)
    x = json_data.copy()
    x.update(convert_to_uppercase)
    if db.cve.count_documents(x) == 0:
        result=db.cve.insert_one(x)
#Step 7 : Tell us that you are done
print('finished inserting recent CVEs')