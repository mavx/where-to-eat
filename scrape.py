#import the library used to query a website
import urllib
import urllib.request
import requests
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
url = 'https://www.zomato.com/kuala-lumpur'
headers = {'user-agent': 'test-app'}

#Query the website and return the html to the variable 'page'
# page = urllib.request.urlopen(url)
page = requests.get(url, headers=headers).text

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, 'html.parser')

# print(soup.prettify())

print('Title', soup.title)
print('titlename', soup.title.name)
print('String', soup.title.string)
print('titleparentname', soup.title.parent.name)
print('p class', soup.p)

print('all as', soup.find_all('a'))
