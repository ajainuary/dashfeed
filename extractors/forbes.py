# import requests
# from bs4 import BeautifulSoup
# from inserttodatabase import push_to_database
# import urllib.request
# import os
# from PIL import Image
# from time import time

# url='https://www.forbes.com/sites/armstrongpaul/2018/04/06/former-south-korean-president-park-geun-hye-handed-24-year-jail-sentence-for-corruption/#a74f746ffe17'
# req = requests.get(url)
# #The category must be extracted from the URL itself
# soup = BeautifulSoup(req.text, 'html.parser')
# title = soup.find('h1', attrs={'class': 'fs-headline speakable-headline'}).get_text().strip()
# subtitle = soup.find('p', attrs={'class': 'speakable-paragraph'}).get_text().strip()
# content = soup.find('article-body-container')
# para = content.findAll('p')
# story=""

# save = ""
# image = (soup.find_all('div',class_='article-body-image'))
# for i in image:
# 	temp = i.find('progressive-image')
# 	cur=temp['src']
# 	fullfilename = os.path.join('../static/', str(time())+".jpg")
# 	urllib.request.urlretrieve(cur,fullfilename)
# 	img = Image.open(fullfilename)
# 	width, height = img.size
# 	img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
# 	img.save(fullfilename)
# 	save = save + str(fullfilename)
# 	save = save + ","
# for x in para:
# 	if x.string is not None:
# 		story=story+"<p>"+x.get_text().strip()+"</p>"
# push_to_database(title,subtitle,story,1,url,save)

import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from time import time


url = 'https://www.forbes.com/'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
print (re)
# links = re.find_all('div',class_='article-block-container')
# print (links)
for i in re:
	try:
		# actlink = i.find('a')
		url = 'http://www.forbes.com'+i['ng-href']
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		print(url)
		headline = soup.find('h1', attrs={'class': 'fs-headline speakable-headline'}).get_text().strip()
		subtitle = soup.find('p', attrs={'class': 'speakable-paragraph'}).get_text().strip()
		para = soup.find('article-body-container')
		story=""
		save = ""
		im = (soup.find_all('div',class_='article-body-image'))
		image = im.find_all('img')
		for i in image:
			cur=i['src']
			curtime = str(time())
			fullfilename = os.path.join('../site/static/', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		for x in para:
			if x.string is not None:
				story=story+"<p>"+x.get_text().strip()+"</p>"
		push_to_database(headline,subtitle,story,1,url,save)
	except:
		pass