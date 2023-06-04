# Advent of Code 2022 Day 12
# https://adventofcode.com/2022/day/12

import time

starting_time = time.time()

lst = [l.strip() for l in open('day12_test.txt')]
print(lst[:5])

alpha = ['abcdefghijklmnopqrstuvwxyz']
start,end = 'S','E'

def neighbors(r,c,arr):
    """Generates list of all neighbors of location in grid
    up, down, left and right"""
    output = list()
    if c > 0: #left
        output.append([r, c - 1])
    if c < len(arr) - 1: #right
        output.append([r, c + 1])
    if r>0:#row above
        output.append([r-1,c])
        '''if c > 0:
            output.append([r-1,c-1])
        if c < len(arr)-1:
            output.append([r-1,c+1])'''
    if r < len(arr)-1: #row below
        output.append([r + 1, c])
        '''if c > 0:
            output.append([r+1,c-1])
        if c < len(arr)-1:
            output.append([r+1,c+1])'''
    return output

def check_no_conflicts(arr,current,new,testing=False):
    '''Returns False if there ARE conflicts'''
    posr,posc = current[0],current[1]
    letter = arr[posr][posc]
    if testing:
        print("letter:",letter)
    r, c = new[0], new[1]
    newletter = arr[r][c]
    if testing:
        print("newletter:", newletter)

    #if starting, go to 'a'
    if letter == "S" and newletter == 'a':
        return False
    #Can't be too far
    if ord(newletter) - ord(letter) > 1:
        if testing:
            print('ord')
        return False
    if loc in locs:
        if testing:
            print('loc in locs')
        return False

def make_path(start,end,arr):
    pos = start
    locs = [pos]
    steps = 0
    while pos != end:
        print("pos:",pos)
        steps += 1
        print("Step",steps,"pos:",pos)
        if steps > 20: return locs
        posr,posc = pos[0],pos[1]
        nbs = neighbors(posr,posc,arr)
        print(nbs)
        for loc in nbs:
            r,c = loc[0],loc[1]
            newletter = arr[r][c]
            print("newletter:",newletter)
            letter = arr[posr][posc]
            print('letter:',letter)
            if letter == "S" and newletter == 'a':
                pos = loc[::]
                print("newpos:", pos)
                locs.append(loc)
                break
            if abs(ord(letter)-ord(newletter))>1:
                print('ord')
                continue

            if loc in locs:
                print('loc in locs')
                continue
            if ord(newletter) > ord(letter):
                pos = loc[::]
                print("newpos:", pos)
                locs.append(loc)
                break
            pos = loc[::]
            print("newpos:",pos)
            locs.append(loc)
            break
    return locs

print(make_path([0,0],[2,4],lst))

for char in 'abcde':
    print(char,ord(char))


#print(neighbors(0,0,lst),neighbors(1,1,lst))

print("Time (secs):",time.time()-starting_time)
