#! /usr/bin/env python3

import re, os

files = os.listdir(os.getcwd())
txt_files = []
reg = re.compile(r'.*\.txt')

for doc in files:
    if reg.search(doc) is not None:
        txt_files.append(doc)

# Write regex to match
search_regex = re.compile(r'\s?\w*\!')   # Matches all words ending in !

for doc in txt_files:
    openned_file = open('{0}/{1}'.format(os.getcwd(), doc))
    contents = openned_file.read()
    string = ''.join(contents)
    found = search_regex.findall(contents)
    fount_str = ' '.join(found)
    if fount_str != '':
        print(fount_str + " ---from file " + doc)
