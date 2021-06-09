#! /usr/bin/env python3

import zipfile, shutil, os, re

# '/Users/asif/Downloads/Automate Boring Stuff with Python/Oraganizing Files'

def copyTxtToNewFolder(folder):

    dir_name = input("Enter new directory name: ")
    os.mkdir('/Users/asif/Downloads/Automate Boring Stuff with Python/' + dir_name)
    print('Copying files...')
    for folder, subfolders, filenames in os.walk(folder):

        # print('Folder' + folder)
        for filename in filenames:
            if filename.endswith('.txt'):
                shutil.copy(folder+"/"+filename, '/Users/asif/Downloads/Automate Boring Stuff with Python/' + dir_name)
    print('Done.')

copyTxtToNewFolder('/Users/asif/Downloads/Automate Boring Stuff with Python/')
