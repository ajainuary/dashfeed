import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from time import time


url = 'http://www.foxnews.com'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('article')
for i in links:
	try:
		curitem = i.find('a')
		url = curitem['href']
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		headline = (soup.find('h1',class_='headline head1')).get_text().strip()
		subtitle = soup.find("div","article-body").find("p").get_text().strip()
		para = soup.find("div","article-body").find_all("p")
		story=""
		save = ""
		image = (soup.find_all('div','embed-media fn-video'))
		for i in image:
			temp = i.find('img')
			cur = temp['src']
			curtime = str(time())
			fullfilename = os.path.join('../site/static', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		for x in para:
			if x.string is not None:
				story=story+"<p>"+x.get_text().strip()+"</p>"
		print(url)
		push_to_database(headline,subtitle,story,1,url,save)
	except:
		pass