# Advent of Code 2022 Day 10
# https://adventofcode.com/2022/day/10

import time

starting_time = time.time()

lst = [l.strip() for l in open('day10.txt')]
#print("length of list:",len(lst))
testlst2 = [l.strip() for l in open('day10_test.txt')]
#print(lst[:5])
testlst = ['noop','addx 3','addx -5']

def cycle(arr,n=10000):
    """Gives the value of X after n cycles given an
    array of commands"""
    cyc = 0
    X = 1
    for comm in arr:
        cyc += 1
        if cyc == n:
            return X
        if comm == 'noop':
            continue
        #addx 2 cycles
        cyc += 1
        if cyc == n:
            return X
        comm_lst = comm.split(' ')
        num = int(comm_lst[-1])
        X += num
        print("cyc:",cyc,"X:",X)
        if cyc == n:
            return X

    return X

#print("test:",cycle(testlst))
cycs = [20,60,100,140,180,220]

def part1():
    total = 0
    for cyc in cycs:
        total += cyc*cycle(lst,cyc)
    #print("total:",total)

px = list() #list for pixels
def render(x,c):
    global px
    if abs(x - (c % 40)) < 2:
        px.append("#")
    else:
        px.append(".")

def part2(arr):
    """Prints a # or a . given an
    array of commands"""
    cyc = 0
    X = 1
    for comm in arr:
        render(X, cyc)
        if comm == 'noop':
            cyc += 1
            continue
        #addx 2 cycles
        cyc += 1
        render(X, cyc)
        comm_lst = comm.split(' ')
        num = int(comm_lst[-1])
        X += num
        #print("cyc:",cyc,"X:",X)
        cyc += 1
        #render(X,cyc)

def part2OLD(arr=lst):
    px = list() #list for pixels
    for cyc in range(1,41):
        if abs(cycle(arr,cyc)-cyc%40) < 2:
            px.append("#")
        else:
            px.append(".")
    for i in range(6):
        print(''.join(px[(40*i):(40*(i+1))]))

part2(lst)
for i in range(6):
    print(''.join(px[(40 * i):(40 * (i + 1))]))
print("Time (secs):",time.time()-starting_time)
