import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from time import time

for i in 1,2,3:
	temp = i;
	url = 'http://blogs.iiit.ac.in/page/'+str(temp)
	response = requests.get(url)
	ret = BeautifulSoup(response.content, 'html.parser')
	links = ret.find_all('h4')
	for i in links:
		try:
			aux = i.find('a')
			url = aux['href']
			newresponse = requests.get(url)
			soup = BeautifulSoup(newresponse.content,'html.parser')
			headline = (soup.find('h1').get_text().strip())
			subtitle = "Life at IIIT"
			para = soup.find_all('p')
			story=""
			save = ""
			image = (soup.find_all('img'))
			save = ""
			for i in image:
				cur=i['src']
				curtime = str(time())
				fullfilename = os.path.join('../site/static', curtime+".jpg")
				urllib.request.urlretrieve(cur,fullfilename)
				save = save + str(curtime+".jpg")
				save = save + ","
			for x in para:
				if x.string is not None:
					story=story+"<p>"+x.get_text().strip()+"</p>"
			if save == "" or story == "":
				raise Exception('No image')
			tags = 'iiit'
			print(url)
			push_to_database(headline,subtitle,story,1,url,tags,save)
		except:
			pass