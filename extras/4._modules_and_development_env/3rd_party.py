import requests
from bs4 import BeautifulSoup

my_response = requests.get('http://www.google.com').content
soup = BeautifulSoup(my_response)
print(soup.prettify())

