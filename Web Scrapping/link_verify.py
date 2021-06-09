#! /usr/bin/env python3

import bs4, requests

url = input('Enter url: ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
print('Links found %s...' %len(links))

fof = []

for link in links:
    print('Checking...')
    try:
        unmade_url = link['href']
        if unmade_url.startswith('http'):
            to_check = unmade_url

        elif unmade_url.startswith('//'):
            to_check = 'https:' + unmade_url

        elif unmade_url.startswith('#'):
            to_check = url + unmade_url

        result = requests.get(to_check)

        if result.status_code == 404:
            fof.append(to_check)

    except:
        pass

print('Links processed these ' + str(len(fof)) + ' returned error 404:')
print('\n'.join(fof))
