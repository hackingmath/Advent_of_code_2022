#Advent of Code 2022 Day 18
#https://adventofcode.com/2022/day/18

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time
from operator import methodcaller

start = time.time()

data = open('day18test.txt').read().strip()
lines = [x for x in data.split('\n')]
lines = [list(map(int,x.split(','))) for x in lines]
print(len(lines),lines)

def shared_sides(a,b,testing=False):
    s = 0
    if testing:
        print(a,b)
    if a[0]==b[0] and a[1]==b[1] and a[2]==b[2]:
        return 6

    if (a[0]==b[0] and a[1]==b[1] and abs(a[2]-b[2]) == 1) or \
            (a[0]==b[0] and a[2]==b[2] and abs(a[1]-b[1]) == 1):
        s += 1
        if testing:
            print("equal x's")
    elif (a[2] == b[2] and a[1]==b[1] and abs(a[0]-b[0]) == 1) or \
            (a[2] == b[2] and a[0]==b[0] and abs(a[1]-b[1]) == 1):
        s += 1
        if testing:
            print("equal y's")
    elif (a[1] == b[1] and a[0]==b[0] and abs(a[2]-b[2]) == 1) or \
            (a[1] == b[1] and a[2]==b[2] and abs(a[0]-b[0]) == 1):
        s += 1
        if testing:
            print("equal z's")
    if testing:
        print("s:",s)
    return s

def part1(testing=False):
    sides = 0
    testlines = [[1,1,1],[2,1,1]]
    for i,cube in enumerate(lines):
        sides += 6
        for j in range(i+1,len(lines)):
            if i == j:
                sides -= 6
                continue
            if testing:
                print("i,j:",i,j)
            #sides += 6
            if testing:
                print("sides:",sides)
            sides -= 2*shared_sides(cube,lines[j],testing)
    print(sides)



def part2(testing=False):
    sidedict = dict()
    for i in range(len(lines)):
        sidedict[i] = 6
    if testing:
        print(sidedict)
    sides = 0
    testlines = [[1, 1, 1], [2, 1, 1]]
    for i, cube in enumerate(lines):
        sides += 6
        for j in range(i + 1, len(lines)):
            if i == j:
                sides -= 6
                continue
            if testing:
                print("i,j:", i, j)
            # sides += 6
            if testing:
                print("sides:", sides)
            shared = shared_sides(cube, lines[j], testing)
            sidedict[i] -= shared
            sidedict[j] -= shared
            sides -= 2 * shared
    for n in sidedict:
        if sidedict[n] == 0:
            print(n,lines[n])
    print(sum(sidedict.values()))
    #print(sides)


#part1()
part2()

print("Time (sec.):",time.time()-start)
