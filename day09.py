# Advent of Code 2022 Day 9
# https://adventofcode.com/2022/day/9

import time
from math import sqrt

starting_time = time.time()

lst = [l.strip() for l in open('day09.txt')]
#print(lst[:5])

testlst = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2']
testlst2 = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']
head1,head2 = [0,0],[0,0] #previous, current
tail = [0,0]
locs = set()
tails = [[0,0] for _ in range(9)]
newtails = [[0,0] for _ in range(9)]
tail_locs = set()

def move_head(movestr):
    global tail,tails
    movelist = movestr.split(' ')
    #head1 = head2

    direction = movelist[0]
    steps = int(movelist[1])
    for i in range(steps):
        head1 = head2[::]  # current becomes previous
        if direction == 'L':
            head2[1] -= 1
        elif direction == 'R':
            head2[1] += 1
        elif direction == 'U':
            head2[0] += 1
        elif direction == 'D':
            head2[0] -= 1

        if distance(head2, tail) >= 2:
            tail = follow(tail,head2)
            newtails[0] = tail #first tail segment moves
        #print("head1,head2:",head1,head2)
        #print("tail:",tail)
        locs.add(1000 * tail[0] + tail[1])

        for i,segment in enumerate(tails):
            if i == 0:
                #newtails[i] = tails[i]
                continue
            if distance(newtails[i-1],tails[i]) >= 2:
                #print(newtails[i-1],tails[i],tails[i-1])
                newtails[i] = follow(segment,tails[i-1])
                #print(newtails[i])
        #print("t:",tails)
        #print("n:",newtails)
        tails = newtails[::]

        tail_locs.add(1000*tails[8][0] + tails[8][1])
    #print("final tails:", tails)



def distance(p1,p2):
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def follow(tail,head):
    dy = head[0] - tail[0]
    dx = head[1] - tail[1]
    if abs(dy) == 2:
        tail[0] += dy//2
        if dx == 1:
            tail[1] += 1
        elif dx == -1:
            tail[1] -= 1
    if abs(dx) == 2:
        tail[1] += dx//2
        if dy == 1:
            tail[0] += 1
        elif dy == -1:
            tail[0] -= 1
    return tail

for move in lst:
    move_head(move)
    #print(locs)
print("part1:",len(locs)) #7043 too high, 6171 too low, 6486 correct.
print("part2:",len(tail_locs))


print("Time (secs):",time.time()-starting_time)
