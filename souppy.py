import requests
from bs4 import BeautifulSoup as bs

# url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los%20Angeles%2C%20CA"

def get_data_from_url(page_num):
	actual_url = ""
	base_url = "https://www.yellowpages.com/search?search_terms=Clubs&geo_location_terms=Dallas%2C+TX"
	if page_num == 0:
		actual_url = base_url
	else:
		actual_url = base_url + "&page=" + str(page_num)
		# print(actual_url)
	return actual_url

def myscrapper(pg):

	r = requests.get(get_data_from_url(pg))

	soup = bs(r.content, 'html.parser')

	g_data = soup.find_all('div', {"class":"info"})

	for item in g_data:
		try:
			print(item.contents[0].find_all("span",{"itemprop": "name"})[0].text)
		except IndexError:
			print("No Name!")
		try:
			print(item.contents[1].find_all("span",{"itemprop": "streetAddress"})[0].text)
		except IndexError:
			print("No StreetAddress!")
		try:
			print(item.contents[1].find_all("span",{"itemprop": "addressLocality"})[0].text.replace(',',''))
		except IndexError:
			print("No Locality!")
		try:
			print(item.contents[1].find_all("span",{"itemprop": "addressRegion"})[0].text)
		except IndexError:
			print("No Region!")
		try:
			print(item.contents[1].find_all("span",{"itemprop": "postalCode"})[0].text)
		except IndexError:
			print("No Region!")
		try:
			print(item.contents[1].find_all("div",{"itemprop": "telephone"})[0].text)
		except IndexError:
			print("No Region!")
		print("---------------------------")

