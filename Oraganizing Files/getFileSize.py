#! /usr/bin/env python3

import os

def getFileSize(folder):

    for folder, subfolders, filenames in os.walk(folder):
        # print('Folder: ' + folder)

        for filename in filenames:
            fileSize = (os.path.getsize(folder+'/'+filename)) >> 20
            if fileSize > 50:
                print(filename + " has size: " + str((os.path.getsize(folder+'/'+filename))/1024) + ' MB')


getFileSize('/Users/asif/Downloads')
