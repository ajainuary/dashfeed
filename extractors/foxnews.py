# import requests
# from bs4 import BeautifulSoup
# from inserttodatabase import push_to_database
# import urllib.request
# import os
# from PIL import Image
# from time import time

# url = 'http://www.foxnews.com/politics/2018/04/06/trade-war-or-war-words-experts-sound-alarm-as-china-promises-to-fight-to-end.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# headline = (soup.find('h1',class_='headline head1')).get_text().strip()
# subtitle = soup.find("div","article-body").find("p").get_text().strip()
# para = soup.find("div","article-body").find_all("p")
# story=""


# save = ""
# image = (soup.find_all('div',class_='m'))
# # image = image.find('img')
# for i in image:
# 	temp = i.find('img')
# 	cur=temp['src']
# 	fullfilename = os.path.join('../static/', str(time())+".jpg")
# 	urllib.request.urlretrieve(cur,fullfilename)
# 	img = Image.open(fullfilename)
# 	width, height = img.size
# 	img = img.resize((320,int((320*height)/width)), Image.ANTIALIAS)
# 	img.save(fullfilename)
# 	save = save + str(fullfilename)
# 	save = save + ","
# 	print (save)
# for x in para:
# 	if x.string is not None:
# 		story=story+"<p>"+x.get_text().strip()+"</p>"
# push_to_database(headline,subtitle,story,1,url,save)

import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time


url = 'http://www.foxnews.com'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('article')
# print (links)
for i in links:
	# try:
		curitem = i.find('a')
		url = curitem['href']
		# print (url)
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		headline = (soup.find('h1',class_='headline head1')).get_text().strip()
		subtitle = soup.find("div","article-body").find("p").get_text().strip()
		para = soup.find("div","article-body").find_all("p")
		story=""
		save = ""
		image = (soup.find_all('img'))
		# image = image.find('img')
		for i in image:
			cur=i['src']
			curtime = str(time())
			fullfilename = os.path.join('../site/static', curtime+".jpg")
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
		print(url)
		push_to_database(headline,subtitle,story,1,url,save)
	# except:
	# 	pass