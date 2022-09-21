#This script scrapes a webpage and returns the title of the page
#The user supplies the webpage url as an argument

import sys
import requests
from bs4 import BeautifulSoup

#Get the url from the command line
url = sys.argv[1]

#Get the webpage
r = requests.get(url)

#Get the title
soup = BeautifulSoup(r.text, 'html.parser')

#Print the title
print(soup.title.string)

