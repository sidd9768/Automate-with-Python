#! /usr/bin/env python3

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter 1 for (heads) or 0 for (tails):')
    guess = input()

GUESS_CONVERTER = {0: 'heads', 1:'tails'}
toss = GUESS_CONVERTER[random.randint(0,1)]
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
