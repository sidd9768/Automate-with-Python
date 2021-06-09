#! /usr/bin/env python3

def picnicTable(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':8000}
picnicTable(picnicItems, 12,5)
