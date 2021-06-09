#! /usr/bin/env python3

import time
market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'red', 'ew':'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        print('The light is: ' + stoplight[key])
        if stoplight[key] == 'green':
            for i in range(3,0,-1):
                time.sleep(1)
                print('Changing in ' + str(i) + ' seconds')
            stoplight[key] = 'yellow'
            print('The light is: ' + stoplight[key])
        elif stoplight[key] == 'yellow':
            for i in range(3,0,-1):
                time.sleep(1)
                print('Changing in ' + str(i) + ' seconds')
            stoplight[key] = 'red'
            print('The light is: ' + stoplight[key])
        elif stoplight[key] == 'red':
            for i in range(3,0,-1):
                time.sleep(1)
                print('Changing in ' + str(i) + ' seconds')
            stoplight[key] = 'green'
            print('The light is: ' + stoplight[key])

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)
