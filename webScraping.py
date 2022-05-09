# step 0:get all the requirements

import csv
import requests
from bs4 import BeautifulSoup
# url = "https://codewithharry.com"

# step 1: Get the HTML
# r = requests.get(url)
# htmlContent = r.content
# print(htmlContent)

# step 2: Parse the HTML
# soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())


# step 3: HTML tree traversal
# Get the title of the html page
# title = soup.title

# commonly used types of objects:
# 1. Tag
# print(type(title))
# 2. NavigableString
# print(type(title.string))
# 3. BeautifulSoup
# print(type(soup))
# 4. Comment

# Get the title of the html page
# title = soup.title

# Get all the paragraphs from the page
# anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p'))  # get first element in the html page
# print(soup.find('p')['class'])  # get classes of any element in the HTML page

# find all the elements with class lead
# print(soup.find_all('p', class_="md:text-base"))

# get the text from the tags/soup
# print(soup.find('p').get_text())

# get the text from the entire page
# print(soup.getText())


# to get the all links on the page
'''
anchors = soup.find_all('a')
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)

'''

# not clear with this
"""markup = "<p> <!-- this is a comment --> </p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))
"""
'''

# This will not run on online IDE

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
'''


# Python program to scrape website
# and save quotes from website

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.findAll('div',
                         attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
