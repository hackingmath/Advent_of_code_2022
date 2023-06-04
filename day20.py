#Advent of Code 2022 Day 20
#https://adventofcode.com/2022/day/20

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

data = open('day20.txt').read().strip()
lines = [int(x) for x in data.split('\n')]
print(len(lines),lines)

testlist= [1, 2, -3, 3, -2, 0, 4]
outlist = lines[::]

def mix(lst,n,testing=False):
    idx = lst.index(n)
    newlst = lst[::]
    newlst.remove(n)
    newlst.insert((idx+n)%len(newlst),n)
    if testing:
        print("n,lst:",n,newlst)
    return newlst

def find_nth(lst,n,testing=False):
    idx = lst.index(0)
    nth = lst[(idx+n)%len(lst)]
    return nth

#for n in [1000,2000,3000]:
    #print(find_nth([-2, 1, 2, -3, 4, 0, 3],n))

#print(mix(testlist,1))


def part1(testing=False):
    global outlist
    for n in lines:
        outlist=mix(outlist,n,testing)
    #print(outlist)
    print("soln:",sum([find_nth(outlist,m,testing) for m in [1000,2000,3000]]))

def part2(testing=False):
    pass

part1()
#part2()

print("Time (s.):",time.time()-start)