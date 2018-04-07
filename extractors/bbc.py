import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time


url = 'http://www.bbc.com/news/world-asia-india-43652304'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

image = (soup.find('img',class_='js-image-replace'))['src']
fullfilename = os.path.join('../static/', str(time())+".jpg")
urllib.request.urlretrieve(image,fullfilename)
img = Image.open(fullfilename)
width, height = img.size
img = img.resize((320,(320*height)/width), Image.ANTIALIAS)

headline = (soup.find('h1',class_='story-body__h1')).get_text().strip()
subtitle = (soup.find(class_='story-body__introduction')).get_text().strip()
para = soup.find("div","story-body__inner").find_all("p")
story=""


save = ""
image = (soup.find_all('img',class_='js-image-replace'))
for i in image:
	cur=i['src']
	fullfilename = os.path.join('../static/', str(time())+".jpg")
	urllib.request.urlretrieve(cur,fullfilename)
	img = Image.open(fullfilename)
	width, height = img.size
	img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
	img.save(fullfilename)
	save = save + str(fullfilename)
	save = save + ","
	print (save)
for x in para:
	if x.string is not None:
		story=story+"<p>"+x.get_text().strip()+"</p>"
push_to_database(headline,subtitle,story,1,url,save)