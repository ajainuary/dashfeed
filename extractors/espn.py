import requests
from bs4 import BeautifulSoup
from inserttodatabase import push_to_database
url = 'http://www.espn.in/commonwealth-games/story/_/id/23044651/sanjita-chanu-wins-india-second-gold-commonwealth-games'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = soup.find("header","article-header").find("h1").get_text().strip()
subtitle = soup.find("div","article-body").find("p").get_text().strip()
para = soup.find("div","article-body").find_all("p")
story=""
for x in para:
	if x.string is not None:
		story=story+x.get_text().strip()
push_to_database(headline,subtitle,story,1,url)