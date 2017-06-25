#import the library used to query a website
import urllib
import urllib.request
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#specify the url
url = 'https://www.zomato.com/kuala-lumpur'

#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(url)

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

print(soup.prettify())
