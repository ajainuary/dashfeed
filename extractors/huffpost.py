import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time

url = 'https://www.huffingtonpost.in/2018/04/06/wont-vote-for-him-again-residents-of-a-small-rajasthan-town-have-a-warning-for-modi-ahead-of-the-2019-polls_a_23404420/?utm_hp_ref=in-homepage'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='headline__title')).get_text().strip()
subtitle = (soup.find('h2',class_='headline__subtitle')).get_text().strip()
para = soup.find("div","post-contents").find_all("p")
story=""

save = ""
image = (soup.find_all('img',class_='image__src'))
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
for x in para:
	if x.string is not None:
		story=story+"<p>"+x.get_text().strip()+"</p>"
push_to_database(headline,subtitle,story,1,url,save)