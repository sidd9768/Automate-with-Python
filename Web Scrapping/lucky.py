#! /usr/bin/env python3

import sys,requests,webbrowser
from bs4 import BeautifulSoup

print('Googling...')  #Display the text while downloading the data
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# print(res.text[:200])
# Retrieve top search result links
soup = BeautifulSoup(res.content, 'html.parser')
print(type(soup))
print(soup.select('body #gsr'))
# Open a browser tab for each result.
linkElems = soup.select('.yuRUbf a')
print(len(linkElems))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print('Opening...')
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
