# Advent of Code 2022 Day 1
# https://adventofcode.com/2022/day/1

import time

starting_time = time.time()

with open('day01.txt') as f:
    lines = f.readlines()
    lst = [x for x in lines]

elves = dict()
elfnum = 0
for n in lst:
    if n == '\n':
        elfnum += 1
    elif elfnum in elves:
        elves[elfnum] += int(n[:-1])
    else:
        elves[elfnum] = int(n[:-1])
# for i in range(5):
#     print(i,elves[i])

#elf0 = [6750,6538,5292,4635,6855,4137,3840,4691,1633,6008,2447,1448,4061]
#print(sum(elf0))
maxelf = max(elves,key=elves.get)
print("Max of elves:",maxelf,elves[maxelf])
# d = {"q": 18, "z": 10, "o": 13}
# print("Max of d:",max(d,key=d.get),d[max(d)])
x = list(elves.values())
x.sort(reverse=True)
print(x[:3],sum(x[:3]))

print("Time (secs):",time.time()-starting_time)
