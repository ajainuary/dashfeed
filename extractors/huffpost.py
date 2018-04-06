import requests
from bs4 import BeautifulSoup
url = 'https://www.huffingtonpost.in/2018/04/06/wont-vote-for-him-again-residents-of-a-small-rajasthan-town-have-a-warning-for-modi-ahead-of-the-2019-polls_a_23404420/?utm_hp_ref=in-homepage'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find('h1',class_='headline__title'))
print("Title :", headline.string)
storybody = (soup.find('h2',class_='headline__subtitle'))
print("Subtitle :",storybody.string)
para = soup.find("div","post-contents").find_all("p")
print('Content:')
for x in para:
	if x.string is not None:
		print(x.string)