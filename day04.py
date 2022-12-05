# Advent of Code 2022 Day 4
# https://adventofcode.com/2022/day/4

import time

starting_time = time.time()

lst = [l.strip() for l in open('day04.txt')]
print(lst[:5])

def separate_pairs(pairstr):
    pairlst = pairstr.split(',')
    return pairlst

def printrange(rangestr):
    rangelst = rangestr.split("-")
    start = int(rangelst[0])
    end = int(rangelst[1])
    return [x for x in range(start,end+1)]

def contained(lst1,lst2):
    return all(item in lst1 for item in lst2) or all(item in lst2 for item in lst1)

def overlap(lst1,lst2):
    return any(item in lst1 for item in lst2) or all(item in lst2 for item in lst1)

def part1():
    total = 0
    for pairstring in lst:
        stringlist = separate_pairs(pairstring)
        #print()
        if contained(printrange(stringlist[0]), printrange(stringlist[1])):
            total += 1
    return total

def part2():
    total = 0
    for pairstring in lst:
        stringlist = separate_pairs(pairstring)
        if overlap(printrange(stringlist[0]), printrange(stringlist[1])):
            total += 1
    return total

print(part1())
print(part2())
print("Time (secs):",time.time()-starting_time)
