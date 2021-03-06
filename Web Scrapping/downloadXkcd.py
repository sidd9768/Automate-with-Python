#! /usr/bin/env python3

import os, requests, bs4

url = 'http://xkcd.com'    # Starting url
os.makedirs('xkcd', exist_ok=True)    # Store the comic in ./xkcd

while not url.endswith('#'):

    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find the comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevlink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevlink.get('href')

print('Done!')
