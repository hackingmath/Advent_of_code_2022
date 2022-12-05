# Advent of Code 2022 Day 5
# https://adventofcode.com/2022/day/5

import time

starting_time = time.time()

lst = [l.strip() for l in open('day05.txt')]
# print(lst[11])

teststacks = ['0','ZN','MCD','P']
teststacks = [list(x) for x in teststacks]
testmoves = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']
stacks = ['0','BLDTWCFM',"NBL",'JCHTLV','SPJW',"ZSCFTLR","WDGBHNZ","FMSPVGCN",'WQRJFVCZ','RPMLH']
stacks = [list(x) for x in stacks]
moves = [x for x in lst[10:]]

def move1(movestr,s = stacks):
    movelst = movestr.split(' ')
    print(movelst)
    num,fromstack,tostack = int(movelst[1]),int(movelst[3]),int(movelst[5])
    print(num,fromstack,tostack)
    for i in range(num):
        s[tostack].append(s[fromstack][-1])
        s[fromstack] = s[fromstack][:-1]
        print(s[tostack])

def move2(movestr,s = stacks):
    movelst = movestr.split(' ')
    print(movelst)
    num,fromstack,tostack = int(movelst[1]),int(movelst[3]),int(movelst[5])
    print(num,fromstack,tostack)
    s[tostack] += s[fromstack][-num:]
    s[fromstack] = s[fromstack][:-num]
    print(s[tostack])


for i,v in enumerate(moves):
    move2(v)

stackstr = ''
for s in stacks:
    if s[-1] != '0':
        stackstr+=s[-1]
print("Soln:",stackstr)


print("Time (secs):",time.time()-starting_time)
