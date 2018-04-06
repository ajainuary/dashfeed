import requests
import csv
from bs4 import BeautifulSoup
data=[]
file = open('bbcnews.csv ', 'w')
writer = csv.writer(file)
data = ['HEADLINE','STORY BODY','IMAGESOURCE','TAG1','TAG2','TAG3']
writer.writerow(data)
url = 'http://www.bbc.com/news/world-asia-india-43652304'
print (url)
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headline = (soup.find(class_='story-body__h1').get_text().strip())
storybody = (soup.find(class_='story-body__introduction').get_text().strip())
imagesrc = (soup.find(class_='js-image-replace')['src'])
data = [headline, storybody,imagesrc]
tags = (soup.find_all(class_='tags-list__tags'))
for i in tags:
    data.append(i.get_text().strip());
writer.writerow(data)
