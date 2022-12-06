# Advent of Code 2022 Day 6
# https://adventofcode.com/2022/day/6

import time

starting_time = time.time()

lst = [l.strip() for l in open('day06.txt')]
msgstr = lst[0]
print(msgstr[:10])

def different(string):
    """Takes a string and returns True if all the characters are
    different"""
    for char in string:
        if string.count(char) > 1:
            return False
    return True

def find_different(string,n):
    """Finds the index of the first character in string after n-differents"""
    idx = n
    while True:
        if different(string[(idx - n):idx]):
            return idx
        idx += 1

#Test
teststrs = ['mjqjpqmgbljsphdztnvjfqwrcgsmlb',
            'bvwbjplbgvbhsrlpgdmjqwftvncz',
            'nppdvjthqldpwncqszvftbrmjlhg',
            'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
            'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
for t in teststrs:
    print(find_different(t,14))

print("Part1:",find_different(msgstr,4))
print("Part2:",find_different(msgstr,14))

print("Time (secs):",time.time()-starting_time)
