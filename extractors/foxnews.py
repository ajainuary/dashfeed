import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url = 'http://www.foxnews.com/politics/2018/04/06/trade-war-or-war-words-experts-sound-alarm-as-china-promises-to-fight-to-end.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='headline head1')).get_text().strip()
subtitle = soup.find("div","article-body").find("p").get_text().strip()
para = soup.find("div","article-body").find_all("p")
story=""
for x in para:
	if x.string is not None:
		story=story+x.get_text().strip()
push_to_database(headline,subtitle,story,1,url)
