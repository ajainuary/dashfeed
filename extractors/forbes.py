import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url='https://www.forbes.com/sites/armstrongpaul/2018/04/06/former-south-korean-president-park-geun-hye-handed-24-year-jail-sentence-for-corruption/#a74f746ffe17'
req = requests.get(url)
#The category must be extracted from the URL itself
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': 'fs-headline speakable-headline'}).get_text().strip()
subtitle = soup.find('p', attrs={'class': 'speakable-paragraph'}).get_text().strip()
content = soup.find('article-body-container')
para = content.findAll('p')
story=""
for x in para:
	story=story+x.get_text().strip()
push_to_database(title,subtitle,story,1,url)
