import requests
from bs4 import BeautifulSoup
url = 'http://www.foxnews.com/politics/2018/04/06/trade-war-or-war-words-experts-sound-alarm-as-china-promises-to-fight-to-end.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='headline head1'))
print("Title :", headline.string)
storybody = soup.find("div","article-body").find("p")
print("Subtitle :",storybody.string)
para = soup.find("div","article-body").find_all("p")
print('Content:')
for x in para:
	if x.string is not None:
		print(x.string)