#! /usr/bin/env python3

import os


for folderName, subfolders, filenames in os.walk('/Users/asif/Downloads/Automate Boring Stuff with Python/Oraganizing Files'):
    print('The current folder is ' + folderName)

    for subfoler in subfolders:
        print('SUBFOLDER OF ' + folderName + ": " + subfoler)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ": " + filename)

    print(" ")
