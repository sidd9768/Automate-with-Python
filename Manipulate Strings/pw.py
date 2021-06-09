#! /usr/bin/env python3

# pw.py - An insecure password locker program.
import pyperclip

PASSWORDS = {'email': 'fjadsakjf3j23jh1', 'blog': 'Vlajskf23482kjhfkss','luggage':'12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # First command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is not account named ' + account)
