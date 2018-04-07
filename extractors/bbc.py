import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url = 'http://www.bbc.com/news/world-asia-india-43652304'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='story-body__h1')).get_text().strip()
subtitle = (soup.find(class_='story-body__introduction')).get_text().strip()
para = soup.find("div","story-body__inner").find_all("p")
story=""
for x in para:
	if x.string is not None:
		story=story+x.get_text().strip()
push_to_database(headline,subtitle,story,1,url)