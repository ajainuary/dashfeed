import requests
from bs4 import BeautifulSoup
url = 'http://www.espn.in/commonwealth-games/story/_/id/23044651/sanjita-chanu-wins-india-second-gold-commonwealth-games'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = soup.find("header","article-header").find("h1")
print("Title :", headline.string)
storybody = soup.find("div","article-body").find("p")
print("Subtitle :",storybody.string)
para = soup.find("div","article-body").find_all("p")
print('Content:')
for x in para:
	if x.string is not None:
		print(x.string)