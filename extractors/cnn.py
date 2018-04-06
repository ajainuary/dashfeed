import requests
import csv
from bs4 import BeautifulSoup
req = requests.get('https://edition.cnn.com/2018/04/04/politics/donald-trump-china-2018-iowa/index.html')
#The category must be extracted from the URL itself
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': 'pg-headline'})
print("Title :", title.string)
content = soup.find('div', attrs={'class': 'l-container'})
subtitle = soup.find('p', attrs={'class': 'zn-body__paragraph speakable'})
print("Subtitle :", subtitle.text.strip())
print("Content :")
para = soup.findAll('div', attrs={'class': 'zn-body__paragraph'})
for x in para:
	if x.string is not None:
		print(x.string)