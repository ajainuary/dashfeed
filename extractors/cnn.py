import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from time import time

url = 'http://edition.cnn.com/'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('li')
# print (links)
for i in links:
	try:
		curitem = i.find('a')
		url = curitem['href']

		url = 'http://edition.cnn.com' + url
		# print(url)
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		headline = (soup.find('h1',class_='pg-headline')).get_text().strip()
		print(headline)
		subtitle = soup.find('p', attrs={'class': 'zn-body__paragraph speakable'}).get_text().strip()
		para = soup.find('div', attrs={'class': 'l-container'}).get_text().strip()
		story=""
		save = ""
		image = (soup.find_all('image','Image__image'))
		print('upar')
		for i in image:
			# temp = i.find('img')
			cur = i['src']
			curtime = str(time())
			fullfilename = os.path.join('../site/static', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		print('niche')
		for x in para:
			if x.string is not None:
				story=story+"<p>"+x.get_text().strip()+"</p>"
		print(url)
		push_to_database(headline,subtitle,story,1,url,save)
	except:
		pass