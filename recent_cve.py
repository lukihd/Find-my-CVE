from pymongo import MongoClient
import requests
import json
import urllib3
from bs4 import BeautifulSoup
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb://root:password@localhost:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db=client.findmycve
#Step 2: Create sample data
last_cve = requests.get("http://www.cvedetails.com/json-feed.php?numrows=10&vendor_id=0&product_id=0&version_id=0&hasexp=1&opec=1&opov=1&opcsrf=1&opfileinc=1&opgpriv=1&opsqli=1&opxss=1&opdirt=1&opmemc=1&ophttprs=1&opbyp=1&opginf=1&opdos=1&orderby=2&cvssscoremin=0")
curl = last_cve.text
curlpur = curl.replace('\n', '').replace('\r', '').replace('\\', '').replace('//', '')
jsondatas = json.loads(curl)
print(jsondatas[2])
for json_data in jsondatas:
    #Step 3: Insert business object directly into MongoDB via isnert_one
    print(json_data['url'])
    url=json_data['url']
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data.decode('utf-8'), "html.parser")
    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="cvssscorestable")
    soup.find('th', string="CVSS Score").decompose() 
    soup.find('th', string="CWE ID").decompose()   
    keys = [th.get_text(strip=True)for th in table.find_all('th')]
    values = [td.get_text(strip=True) for td in table.find_all('td')]
    d = dict(zip(keys, values))
    print(d)
    x = json_data.copy()
    x.update(d)
    result=db.reviews.insert_one(x)
#Step 5: Tell us that you are done
print('finished inserting recent CVEs')