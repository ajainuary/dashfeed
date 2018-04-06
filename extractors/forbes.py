import requests
import csv
from bs4 import BeautifulSoup
req = requests.get('https://www.forbes.com/sites/armstrongpaul/2018/04/06/former-south-korean-president-park-geun-hye-handed-24-year-jail-sentence-for-corruption/#a74f746ffe17')
#The category must be extracted from the URL itself
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': 'fs-headline speakable-headline'})
print("Title :", title.string)
subtitle = soup.find('p', attrs={'class': 'speakable-paragraph'})
print("Subtitle :", subtitle.text.strip())
print("Content :")
content = soup.find('article-body-container')
para = content.findAll('p')
for x in para:
	print(x.text.strip())