# import requests
# from bs4 import BeautifulSoup
# from inserttodatabase import push_to_database
# import urllib.request
# import os
# from PIL import Image
# from time import time


# url='https://edition.cnn.com/2018/04/04/politics/donald-trump-china-2018-iowa/index.html'
# req = requests.get(url)
# #The category must be extracted from the URL itself
# soup = BeautifulSoup(req.text, 'html.parser')
# title = soup.find('h1', attrs={'class': 'pg-headline'}).get_text().strip()
# content = soup.find('div', attrs={'class': 'l-container'}).get_text().strip()
# subtitle = soup.find('p', attrs={'class': 'zn-body__paragraph speakable'}).get_text().strip()
# story=""
# para = soup.findAll('div', attrs={'class': 'zn-body__paragraph'})


# save = ""
# image = (soup.find_all('img',class_='media__image media__image--responsive'))
# for i in image:
# 	cur=i['src']
# 	print (cur)
# 	fullfilename = os.path.join('../static/', str(time())+"jpg")
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

# push_to_database(title,subtitle,story,1,url,save)

import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
import urllib.request
import os
from PIL import Image
from time import time


url = 'http://edition.cnn.com'
response = requests.get(url)
re = BeautifulSoup(response.content, 'html.parser')
links = re.find_all('div',class_='media')
print (links)
for i in links:
	# try:
		cururl = i.find('a')
		url = 'http://edition.cnn.com'+cururl['href']
		print (url)
		newresponse = requests.get(url)
		soup = BeautifulSoup(newresponse.content,'html.parser')
		headline = (soup.find('h1',class_='story-body__h1')).get_text().strip()
		subtitle = (soup.find(class_='story-body__introduction')).get_text().strip()
		para = soup.find("div","story-body__inner").find_all("p")
		story=""
		save = ""
		image = (soup.find_all('img',class_='js-image-replace'))
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
		push_to_database(headline,subtitle,story,1,url,save)
	# except:
	# 	pass