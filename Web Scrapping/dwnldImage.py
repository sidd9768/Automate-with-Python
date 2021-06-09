#! /usr/bin/env python3

import os, sys, requests, bs4
from selenium import webdriver

user_search = sys.argv[1:]
url = 'http://imgur.com/search?q='+ " ".join(user_search)
os.makedirs(" ".join(user_search), exist_ok=True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imageElem = soup.select('.image-list-link img')

if imageElem == []:
    print('Could not find an image...')
else:
    for i in range(len(imageElem)):
        print('Remaining: ' + str(len(imageElem) - (i+1)))
        image_url = 'http:' + imageElem[i].get('src')
        print('Downloading image %s...' % i)
        res = requests.get(image_url)
        res.raise_for_status()

        imageFile = open(os.path.join(" ".join(user_search), os.path.basename(image_url)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

print('Done...')
