# Advent of Code 2022 Day 3
# https://adventofcode.com/2022/day/3

import time

starting_time = time.time()

lst = [l.strip() for l in open('day03.txt')]
print(lst[:5])

test_sacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw']
alpha = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def part1(s):
    """Separates two compartments,finds common letter, returns value"""
    l = len(s)
    c1,c2 = s[:l//2],s[l//2:]
    #print(c1,c2)
    for c in c1:
        if c in c2:
            return alpha.index(c)

def part2(list3):
    for c in list3[0]:
        if c in list3[1] and c in list3[2]:
            return alpha.index(c)

#print(part1('vJrwpWtwJgWrhcsFMMfFFhFp'))
total = 0
for sack in lst:
    total += part1(sack)
print("Part 1 total:", total)

total2 = 0
lst2 = list()
i = 0
while i < len(lst):
    lst2.append(lst[i:i+3])
    i += 3
for triple in lst2:
    total2 += part2(triple)
print("Part 2 total:", total2)

print("Time (secs):",time.time()-starting_time)
