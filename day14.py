# Advent of Code 2022 Day 12
# https://adventofcode.com/2022/day/12

import time

starting_time = time.time()

data = [l.strip() for l in open('day14.txt')]
teststr = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

#print(data[:5])

testlist = [[[498,4],[498,6],[496,6]],[[503,4],[502,4],[502,9],[494,9]]]

raw = [l.strip('\n') for l in data]
#lst = [int(c) for c in l.split('->') for l in data]

lst = list()
for i,line in enumerate(raw):
    newline = []
    for pair in line.split('->'):
        intpair = [int(c) for c in pair.split(',')]
        newline.append(intpair)
    lst.append(newline)
print(lst[:1])

def addSand(a,b):
    if a[0] < b[0]:
        for i in range(a[0],b[0]+1):
            sandset.add((i,a[1]))
    elif a[0] > b[0]:
        for i in range(b[0],a[0]+1):
            sandset.add((i,a[1]))
    else:
        if a[1] < b[1]:
            for i in range(a[1], b[1] + 1):
                sandset.add((a[0],i))
        elif a[1] > b[1]:
            for i in range(b[1], a[1] + 1):
                sandset.add((a[0],i))
    #part 2
    for i in range(-10000,10000):
        sandset.add((i, 168))

def dropSand():
    """Highest y is 166, so floor is 168"""
    for drops in range(100000):
        sx, sy = 500, -1
        while True:
            #print("drop",drops)
            highest_y = 0
            #print("sy:",sy)
            if (sx,sy+1) not in sandset:
                sy += 1
            elif (sx-1,sy+1) not in sandset:
                sx,sy = sx-1,sy+1
                if sy>highest_y:
                    highest_y = sy
            elif (sx+1,sy+1) not in sandset:
                sx, sy = sx+1,sy+1
                if sy>highest_y:
                    highest_y = sy
            else: break
        if (sx,sy) == (500, 0):
            return drops
            #part 1:
            #if sy >= 175:
                #return drops-1,highest_y #solution: 825
        sandset.add((sx,sy))
        # if drops % 1000 == 0:
        #     print(drops,"drops.")

def dropSandOLD():
    """Highest y is 161, so floor is 163"""
    drops = 1
    while True:
        #print("drop",drops)
        dropping = True
        highest_y = 0
        sx,sy = 500,-1
        while dropping:
            #print("sy:",sy)
            sy += 1
            if sy == 168: #maxy + 2
                sandset.add((sx, sy - 1))
                dropping = False
            elif (sx,sy) in sandset:
                if (sx-1,sy) not in sandset:
                    sx, sy = sx-1,sy
                    if sy>highest_y:
                        highest_y = sy
                elif (sx+1,sy) not in sandset:
                    sx, sy = sx+1,sy
                    if sy>highest_y:
                        highest_y = sy

                else:
                    sandset.add((sx,sy-1))
                    if sy-1 == 0:
                        return drops
                    if sy-1>highest_y:
                        highest_y = sy-1
                    #print("new:",[sx,sy-1])
                    dropping = False
            #part 1:
            #if sy >= 175:
                #return drops-1,highest_y #solution: 825
        drops += 1
        if drops % 100 == 0:
            print(drops,"drops.")

sandset = set()
for line in lst:
    for i,pair in enumerate(line):
        if pair != line[-1]: #if it's not the last in the line
            addSand(pair,line[i+1]) #add the next one in line

maxy = 0
for pair in sandset:
    if pair[1] > maxy:
        maxy = pair[1]
print("max y:",maxy) #166 in my dataset

#print("sandlist:",sandlist)
print("Part2:",dropSandOLD())
print("Time (secs):",time.time()-starting_time)
