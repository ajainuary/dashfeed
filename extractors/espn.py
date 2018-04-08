import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time


url = 'https://www.espn.in'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('article',class_='contentItem')
# print (links)
for i in links:
	try:
		curitem = i.find('a')
		# print (curitem)
		url = 'http://www.espn.in'+curitem['href']
		# print(url)
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		# print(url)
		headline = soup.find("header","article-header").find("h1").get_text().strip()
		subtitle = soup.find("div","article-body").find("p").get_text().strip()
		para = soup.find("div","article-body").find_all("p")
		story=""
		save = ""
		image = (soup.find_all('div',class_='img-wrap'))
		print (image)
		for i in image:
			curitem = image.find('img')
			cur=curitem['src']
			print (cur)
			curtime = str(time())
			fullfilename = os.path.join('../site/static/', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			img = Image.open(fullfilename)
			width, height = img.size
			img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
			img.save(fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		for x in para:
			if x.string is not None:
				story=story+"<p>"+x.get_text().strip()+"</p>"
		push_to_database(headline,subtitle,story,1,url,save)
	except:
		pass