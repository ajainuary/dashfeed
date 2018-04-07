import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url='https://edition.cnn.com/2018/04/04/politics/donald-trump-china-2018-iowa/index.html'
req = requests.get(url)
#The category must be extracted from the URL itself
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.find('h1', attrs={'class': 'pg-headline'}).get_text().strip()
content = soup.find('div', attrs={'class': 'l-container'}).get_text().strip()
subtitle = soup.find('p', attrs={'class': 'zn-body__paragraph speakable'}).get_text().strip()
story=""
para = soup.findAll('div', attrs={'class': 'zn-body__paragraph'})
for x in para:
	if x.string is not None:
		story=story+"<p>"+x.get_text().strip()+"</p>"
push_to_database(title,subtitle,story,1,url)
