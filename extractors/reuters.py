import requests
import re
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url='https://www.reuters.com/article/us-ibm-blockchain/ibm-joins-group-building-a-blockchain-based-global-identity-network-idUSKCN1HC2LM'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': re.compile('headline.*')}).get_text().strip()
content = soup.find('div', attrs={'class': re.compile('body.*')})
subtitle = content.find('p').get_text().strip()
para = content.findAll('p')
story=""
for x in para:
	if x.string is not None:
		story=story+"<p>"+x.get_text().strip()+"</p>"
push_to_database(title,subtitle,story,1,url)
