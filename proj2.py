#proj2.py
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import json
 


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

count=0
for story_heading in soup.find_all(class_="story-heading"):
	print (story_heading.get_text().strip())
	count+=1
	if count == 10:
		break

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url2 = "https://www.michigandaily.com"
r2 = requests.get(base_url2)
soup2 = BeautifulSoup(r2.text, "html.parser")

div=soup2.find(class_="view view-most-read view-id-most_read view-display-id-panel_pane_1 view-dom-id-99658157999dd0ac5aa62c2b284dd266")
for li in div.find_all('li'):
	print(li.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url3 = "http://newmantaylor.com/gallery.html"
r3 = requests.get(base_url3)
soup3 = BeautifulSoup(r3.text, "html.parser")

for img in soup3.find_all('img'):
	try:
		print(img['alt'].strip())
	except:
		print("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
base_url4="https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
href_list=[]
for num in range(0,6):
	if num == 0:
		full_url=base_url4
	else:
		full_url=base_url4+"&page="+str(num)
	
	r4 = urllib.request.Request(full_url, None, {'User-Agent': 'SI_CLASS'})
	uhand = urllib.request.urlopen(r4)
	html = uhand.read()
	soup4 = BeautifulSoup(html, 'html.parser')

	for a in soup4.find_all('a'):
		if a.get_text()=="Contact Details":
			href_list.append(a['href'])

base_url5="https://www.si.umich.edu"
ct=0
for node in href_list:
	full_url2=base_url5+node
	r5 = urllib.request.Request(full_url2, None, {'User-Agent': 'SI_CLASS'})
	uhand2 = urllib.request.urlopen(r5)
	html2 = uhand2.read()
	soup5 = BeautifulSoup(html2, 'html.parser')

	for a in soup5.find_all('a'):
		if a.get('href') and a.get('href').startswith('mailto:'):
			ct+=1
			print(ct,a.get_text())