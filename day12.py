# Advent of Code 2022 Day 12
# https://adventofcode.com/2022/day/12
#Adapted from Jonathan Paulson's video 1/22/23
#https://www.youtube.com/watch?v=DRODVXPgUcI

import time
from collections import defaultdict, deque

starting_time = time.time()

lst = [l.strip() for l in open('day12.txt')]
print(lst[:5])

G = list()
for line in lst:
    G.append(line)
R,C = len(G),len(G[0])

#Assign elevation levels for each cell
E = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S': #if it's the start
            E[r][c] = 1 #elevation is 1
        elif G[r][c] == 'E': #if it's the end
            E[r][c] = 26 #elevation is 26
        else: #otherwise it's the num value of the letter
            E[r][c] = ord(G[r][c]) - ord('a') + 1

def bfs(part):
    Q = deque()
    for r in range(R):
        for c in range(C):
            if E[r][c] == 1 and (part == 2 or G[r][c] =='S'):
                Q.append(((r,c),0))
    S = set()
    while Q:
        (r,c),d = Q.popleft()
        if (r,c) in S:
            continue
        S.add((r,c))
        if G[r][c] == "E":
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and E[rr][cc]<=1+E[r][c]:
                Q.append(((rr,cc),d+1))



print("Part 1:",bfs(1))
print("Part 2:",bfs(2))

print("Time (secs):",time.time()-starting_time)
