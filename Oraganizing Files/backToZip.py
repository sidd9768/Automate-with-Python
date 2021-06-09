#! /usr/bin/env python3

# backToZip.py - Copies an entire folder and its contents into a
# ZIP file whose filename increments.

import zipfile, os

def backToZip(folder):
    # Backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder)   # make sure the folder is absolute

    # Figure out the filename this code should be based on
    # what files already exist.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # Creating the ZIP file
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldernames, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldernames))
        # Add the current folder to the ZIP file
        backupZip.write(foldernames)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldernames, filename))
    backupZip.close()
        

    print('Done.')

backToZip('/Users/asif/Downloads/Automate Boring Stuff with Python/Oraganizing Files')
