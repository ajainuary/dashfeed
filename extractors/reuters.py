import requests
import csv
import re
from bs4 import BeautifulSoup
req = requests.get('https://www.reuters.com/article/us-ibm-blockchain/ibm-joins-group-building-a-blockchain-based-global-identity-network-idUSKCN1HC2LM')
#The category must be extracted from the URL itself
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': re.compile('headline.*')})
print("Title :", title.string)
content = soup.find('div', attrs={'class': re.compile('body.*')})
subtitle = content.find('p')
print("Subtitle :", subtitle.text.strip())
print("Content :")
para = content.findAll('p')
for x in para:
	print(x.text.strip())