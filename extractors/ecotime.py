import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from time import time

url = 'https://economictimes.indiatimes.com/'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
aux = re.find('div',class_='tabsContent')
links = aux.find_all('li')
for i in links:
	try:
		cur = i.find('a')
		url = 'https://economictimes.indiatimes.com'+cur['href']
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		headline = (soup.find('h1',class_='clearfix title')).get_text().strip()
		subtitle = (soup.find('figcaption')).get_text().strip()
		para = soup.find("div",class_='section1').get_text().strip()
		save = ""
		story = ""
		story = soup.find("div",class_="Normal").get_text().strip()
		image = soup.find_all('figure')
		for i in image:
			temp = i.find('img')
			cur = temp['src']
			cur = cur.replace('width-300', 'width-600')
			curtime = str(time())
			fullfilename = os.path.join('../site/static', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		if save == "" or story == "":
			raise Exception('No image')
		push_to_database(headline,subtitle,para,1,url,save)
	except:
		pass