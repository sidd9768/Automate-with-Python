#! /usr/bin/env python3

import os,zipfile

def countFiles(folder):

    txtFiles = []
    pyFiles = []
    folders = []

    BackupTxtAndPy = zipfile.ZipFile('txtAndPy.zip', 'w')
    for folder, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            folders.append(subfolder)
        for filename in filenames:
            if filename.endswith('.txt'):
                BackupTxtAndPy.write(filename)
                txtFiles.append(filename)
            elif filename.endswith('.py'):
                # BackupTxtAndPy.write(filename)
                pyFiles.append(filename)
    BackupTxtAndPy.close

    print('=============== The txt files are: ===============')
    txtnum = 1
    for txt in txtFiles:
        print(str(txtnum) + ". " + str(txt))
        txtnum += 1

    print('=============== The py files are: ===============')
    pynum = 1
    for py in pyFiles:
        print(str(pynum) + ". " + str(py))
        pynum += 1

    print('=============== The folders are: ===============')
    folnum = 1
    for fol in folders:
        print(str(folnum) + ". " + str(fol))
        folnum += 1


countFiles('/Users/asif/Downloads/Automate Boring Stuff with Python/')
