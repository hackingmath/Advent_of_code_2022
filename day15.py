import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
import time

start = time.time()

data = open('day15.txt').read().strip()
lines = [x for x in data.split('\n')]
print(lines[:3])
lst = list()
for line in lines:
    line = line.split(" ")
    for i,v in enumerate(line):
        sx,sy,bx,by = line[2][2:-1],line[3][2:-1],line[8][2:-1],line[9][2:]
    lst.append([sx,sy,bx,by])
print(lst[:3])

xset = set()
def blackout(s,b,lset):
    """Takes a sensor position, the nearest beacon
    and calculates the Manhattan distance d. Then it puts all
    the locations d units from it into the list lst."""
    d = abs(s[1]-b[1]) + abs(s[0]-b[0])
    print("d:",d)
    for i in range(d+1):
        lset.add((s[0],s[1]-i)) #vertical line up
        lset.add((s[0],s[1]+i)) #vertical line down
        for j in range(d+ 1-i):#
            lset.add((s[0]+j,s[1]+i)) #right,down
            lset.add((s[0] - j, s[1] + i))  # left,down
            lset.add((s[0]+ j,s[1] - i))  # right,up
            lset.add((s[0] - j, s[1] - i))  # left,up
            #lst.append(((s[0] + d - i), (s[1] - i)))  # right,up
            #lst.append(((s[0] - d + i), (s[1] - i)))  # left,up
            #lst.append(((s[0] + d - i), (s[1] + i)))  # right,down

blackout([8,7],[2,10],xset)
#print(xlist)
print(len(xset))
print(xset)
for pair in xset:
    if pair[1] == 10:
        print(pair)
total = 0
for pair in xset:
    if pair[1] == 10:
        total += 1
print("total:",total)
#print(lines[0].split(" "))




print("Time (s.):",time.time()-start)

#Output:
