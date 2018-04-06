import requests
from bs4 import BeautifulSoup
url = 'http://www.bbc.com/news/world-asia-india-43652304'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='story-body__h1'))
print("Title :", headline.string)
storybody = (soup.find(class_='story-body__introduction'))
print("Subtitle :",storybody.string)
para = soup.find("div","story-body__inner").find_all("p")
print('Content:')
for x in para:
	if x.string is not None:
		print(x.string)