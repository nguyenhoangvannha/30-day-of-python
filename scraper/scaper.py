# -*- coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.udemy.com/topic/android-development/?p='
page = 2
url = base_url + str(page)

free = requests.get(url)
print(free.status_code)
free_soup = BeautifulSoup(free.text, 'html.parser')
#print(free_soup.prettify())
for title in free_soup.findAll('div',{'class':'thread-title-cell'}):
	print(title.text)
	link = title.find('a', href = True)
	print(link['href'])
	