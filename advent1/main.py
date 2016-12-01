location = [0, 0]
places_weve_been = [(0, 0)]


dir = 'n'


input0 = 'R2, L3'
input1 = 'R5, L5, R5, R3'
input2 = 'R2, R2, R2'
input3 = 'R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3'
input4 = 'R8, R4, R4, R8'

def get_dir(turn, dir):
    #print turn, dir
    if dir == 'n':
        if turn == "r":
            dir = 'e'
        else:
            dir = 'w'
    elif dir == 'e':
        if turn == "r":
            dir = 's'
        else:
            dir = 'n'
    elif dir == 's':
        if turn == "r":
            dir = 'w'
        else:
            dir = 'e'
    elif dir == 'w':
        if turn == "r":
            dir = 'n'
        else:
            dir = 's'
    return dir

def go(distance, dir, location, places_weve_been):
    if dir == 'n':
        for i in range(distance):
            location[1] += 1
            places_weve_been.append((location[0], location[1]))
        #location[1] += distance
    elif dir == 'e':
        for i in range(distance):
            location[0] += 1
            places_weve_been.append((location[0], location[1]))
        #location[0] += distance
    elif dir == 's':
        for i in range(distance):
            location[1] -= 1
            places_weve_been.append((location[0], location[1]))
        #location[1] -= distance
    elif dir == 'w':
        for i in range(distance):
            location[0] -= 1
            places_weve_been.append((location[0], location[1]))
        #location[0] -= distance

    return [location, places_weve_been]

for input in input3.split(', '):
    turn = input[0].lower()
    distance = input[1::]

    dir = get_dir(turn, dir)
    ret = go(int(distance), dir, location, places_weve_been)
    location = ret[0]
    places_weve_been = ret[1]

    #print dir, location

print abs(location[0]) + abs(location[1])

print places_weve_been

import collections
for place in places_weve_been:
    count = 0
    for item in places_weve_been:
        if item == place:
            count += 1

    if count > 1:
        print place
        break

print abs(place[0]) + abs(place[1])