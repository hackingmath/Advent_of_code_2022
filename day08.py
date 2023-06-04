# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8

import time

starting_time = time.time()

lst = [l.strip() for l in open('day08.txt')]
print(lst[:5])

def visible(r,c,arr,test=False):
    """Returns True if larger than any trees in r,c
    from one direction."""
    visible = False
    height = int(arr[r][c])
    if test:
        print("height:",height)
    #left
    for i in range(c):
        if test:
            print("left",r,i,arr[r][i])
        if int(arr[r][i]) >= height:
            visible = False
            if test:
                print("not visible")
            break
        elif i == c-1:
            return True
    # right
    for i in range(c+1,len(arr[0])):
        if test:
            print("right",r,i,arr[r][i])
        if int(arr[r][i]) >= height:
            visible = False
            break
        if i == len(arr[0])-1:
            return True
    # top
    for i in range(r):
        if test:
            print("top",i,c,arr[i][c])
        if int(arr[i][c]) >= height:
            visible = False
            break
        elif i == r-1:
            return True
    # bottom
    for i in range(r+1,len(arr)):
        if test:
            print("bottom",i,c,arr[i][c])
        if int(arr[i][c]) >= height:
            visible = False
            break
        if i == len(arr)-1:
            return True
    return False

def viewable(r,c,arr,test=False):
    """Returns product of number of trees viewable
     in each direction."""
    height = int(arr[r][c])
    total = 0
    if test:
        print("r,c:",r,c)
        print("height:",height)
    #left
    left = 0
    for i in range(c-1,-1,-1):
        left += 1
        if test:
            print("left",r,i,arr[r][i])
        if int(arr[r][i]) >= height:
            if test:
                print("blocked")
            break
    if test:
        print("left score:", left)
    # right
    right = 0
    for i in range(c+1,len(arr[0])):
        right += 1
        if test:
            print("right",r,i,arr[r][i])
        if int(arr[r][i]) >= height:
            break
    if test:
        print("right score:", right)
    # top
    top = 0
    for i in range(r-1,-1,-1):
        top += 1
        if test:
            print("top",i,c,arr[i][c])
        if int(arr[i][c]) >= height:
            break
    if test:
        print("top score:", top)
    # bottom
    bottom = 0
    for i in range(r+1,len(arr)):
        bottom += 1
        if test:
            print("bottom",i,c,arr[i][c])
        if int(arr[i][c]) >= height:
            break
    if test:
        print("bottom score:", bottom)
    score = left*right*top*bottom
    if test:
        print("score:",score)
    return score

testlst = ['30373','25512','65332','33549','35390']

def part1(arr):
    visibles = 0

    test = False

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if r in [0,len(arr)-1]:
                if test:
                    print(r,c)
                visibles += 1
            elif c in [0,len(arr[0]) - 1]:
                if test:
                    print(r,c)
                visibles += 1
            elif visible(r,c,arr,test):
                if test:
                    print(r,c)
                visibles += 1

    print("Visibles: ",visibles)
    #first try 1255 was too low
    #1829 correct

def part2(arr,test=False):
    scores = list()

    for r in range(len(arr)):
        for c in range(len(arr[0])):
             scores.append(viewable(r,c,arr,test))
    if test:
        print(scores)
    print("Score: ",max(scores))
    #First try 600237 too high
    #291840 correct

# testlst = ['30373','25512','65332','33549','35390']
# print(visible(1,2,testlst,True))

#part1(lst)
part2(lst)

print("Time (secs):",time.time()-starting_time)
