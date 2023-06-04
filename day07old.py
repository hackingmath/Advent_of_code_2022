# Advent of Code 2022 Day 7
# https://adventofcode.com/2022/day/7

import time

starting_time = time.time()

lst = [l.strip() for l in open('day07.txt')]
print(lst[:5])

folder = list() #current folder
folders_dict = dict()
sizes = dict() #sizes of files

for step in lst[:10]:
    if step.startswith("$ cd"):
        if step[5] == '/':
            folder = ['main']
        elif step[5:6] == '..':
            folder.pop() #go back one folder
        else:

            step.split(' ')
            folder.append(step[1]) #new current folder
            folders_dict[step[1]] = dict()
    elif step.startswith('$ ls'):
            continue


    elif step.startswith('dir'):
        folder.append(step[4:]) #subfolder

    else: #number
        step = step.split(' ')
        sizes[step[1]] = int(step[0])

def calc_size(x):
    for folder in folders_dict:
        return

print("Folder:",folder)
print("Folders Dict:",folders_dict)

print("Time (secs):",time.time()-starting_time)
