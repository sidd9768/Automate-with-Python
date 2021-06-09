#! /usr/bin/env python3

import re, os
filename = input('Enter the name of the file: ')
file = open('{0}/{1}.txt'.format(os.getcwd(), filename))
sent = file.read()
file.close()

reg = re.compile(r'noun|adjective|verb|adverb')
mad = re.findall(reg, sent)

for word in mad:
    upd_word = input("Enter " + word + ": ")
    sent = sent.replace(word, upd_word,1)

print(sent)
