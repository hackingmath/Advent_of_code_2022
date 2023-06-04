# Advent of Code 2022 Day 7
# https://adventofcode.com/2022/day/7
#Adapted from Jonathan Paulson's video
# https://www.youtube.com/watch?v=ZPM5xclRInk

import time
from collections import defaultdict

starting_time = time.time()

lst = [l for l in open('day07.txt').read().strip().split('\n')]
#print(lst[:5])

SZ = defaultdict(int)
path = list()
for line in lst:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])
        #add this file's size to the current directory and the size of
        #all parents
        for i in range(1,len(path)+1):
            SZ['/'.join(path[:i])] += sz

max_used = 70000000 - 30000000
total_used = SZ['/']
need_to_free = total_used - max_used

p1 = 0
p2 = 1e9
for k,v in SZ.items():
    if v>=need_to_free:
        p2 = min(p2,v)
    if v<= 100000:
        p1+=v

print(p1)
print(p2)

print("Time (secs):",time.time()-starting_time)
