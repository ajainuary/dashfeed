# import requests
# import re
# from bs4 import BeautifulSoup
# from inserttodatabase import push_to_database
# import urllib.request
# import os
# from PIL import Image
# from time import time
# import cssutils

# url='https://www.reuters.com/article/us-ibm-blockchain/ibm-joins-group-building-a-blockchain-based-global-identity-network-idUSKCN1HC2LM'
# req = requests.get(url)
# soup = BeautifulSoup(req.text, 'html.parser')
# title = soup.find('h1', attrs={'class': re.compile('headline.*')}).get_text().strip()
# content = soup.find('div', attrs={'class': re.compile('body.*')})
# subtitle = content.find('p').get_text().strip()
# 		para = content.findAll('p')
# story=""

# save = ""
# image = (soup.find_all('div',class_='image_1KsYy cover_3hgft fallback_2kFne'))
# for i in image:
# 	temp = i['style']
# 	temp1 = cssutils.parseStyle(temp)
# 	temp2 = temp1['background-image']
# 	cur = temp2['url']
# 	print(cur)
# 	fullfilename = os.path.join('../static/', str(time())+".jpg")
# 	urllib.request.urlretrieve(cur,fullfilename)
# 	img = Image.open(fullfilename)
# 	width, height = img.size
# 	img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
# 	img.save(fullfilename)
# 	save = save + str(fullfilename)
# 	save = save + ","
# 	print(save)
# for x in para:
# 	if x.string is not None:
# 		story=story+"<p>"+x.get_text().strip()+"</p>"
# push_to_database(title,subtitle,story,1,url,save


import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time
import cssutils

url = 'https://www.reuters.com'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('div',class_='story-content')
for i in links:
	try:
		curlink = i.find('a')
		url = 'http://www.reuters.com'+curlink['href']
		print (url)
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		# print(url)
		headline = soup.find('h1', attrs={'class': 'headline_2zdFM'}).get_text().strip()
		subtitle = soup.find('p').get_text().strip()
		para = soup.findAll('p')
		story=""
		save = ""
		image = (soup.find_all('div',class_='container_1Z7A0'))
		for i in image:
			# print ('dsa')
			# temp = i['style']
			# temp1 = cssutils.parseStyle(temp)
			# temp2 = temp1['background-image']
			# temp2 = temp2.replace('url(', '').replace(')', '')
			temp2 = i.find('img') 
			cur = 'https:'+temp2['src']
			print(cur)
			# print(cur)
			# cur=i['src']
			curtime = str(time())
			fullfilename = os.path.join('../site/static/', curtime+".jpg")
			urllib.request.urlretrieve(cur,fullfilename)
			# img = Image.open(fullfilename)
			# width, height = img.size
			# img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
			# img.save(fullfilename)
			save = save + str(curtime+".jpg")
			save = save + ","
		for x in para:
			if x.string is not None:
				story=story+"<p>"+x.get_text().strip()+"</p>"
		push_to_database(headline,subtitle,story,1,url,save)
	except:
		pass