#! /usr/bin/env python3

# multiclipboard - Saves and loads pieces of text to the multiclipboard
# Usage: py.exe mcd.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcd.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcd.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcdShelf = shelve.open('mcd')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcdShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcdShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcdShelf.keys())))
        print(str(list(mcdShelf.keys())))
    elif sys.argv[1] in mcdShelf:
        pyperclip.copy(mcdShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for key in mcdShelf:
            mcdShelf.pop(key)

mcdShelf.close()
