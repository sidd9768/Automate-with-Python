allGuests = {'Alice': {'apples':5, 'pretzels':12},
            'Bob': {'ham Sandwiches':3, 'apples':2},
            'Carol': {'cups':3, 'apples pies':1}}


def totalBrought(guests, items):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(items,0)

    return num_brought

print('Number of things being brought: ')
print(' - Apples                ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                  ' + str(totalBrought(allGuests, 'cups')))
print(' - cakes                 ' + str(totalBrought(allGuests, 'cak Sandwiches')))
print(' - Ham Sandwiches        ' + str(totalBrought(allGuests, 'ham Sandwiches')))
print(' - Apples Pies           ' + str(totalBrought(allGuests, 'apples pies')))
