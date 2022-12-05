# Advent of Code 2022 Day 2
# https://adventofcode.com/2022/day/2

import time

starting_time = time.time()

lst = [l.strip() for l in open('day02.txt')]
print(lst[:5])

def points(game_str):
    """Calculates the number of points resulting from given game string"""
    if game_str[0] == 'A': #rock
        if game_str[2] == 'X': #rock
            return 3 + 1 #tie + rock
        elif game_str[2] == 'Y': #paper
            return 6 + 2 #win + paper
        else:
            return 0 + 3 #loss + scissors
    elif game_str[0] == 'B': #paper
        if game_str[2] == 'X':  # rock
            return 0 + 1  # loss + rock
        elif game_str[2] == 'Y':  # paper
            return 3 + 2  # tie + paper
        else:
            return 6 + 3  # loss + scissors
    else: #scissors
        if game_str[2] == 'X':  # rock
            return 6 + 1  # win + rock
        elif game_str[2] == 'Y':  # paper
            return 0 + 2  # loss + paper
        else:
            return 3 + 3  # tie + scissors

def part2(game_str):
    if game_str[0] == 'A': #rock
        if game_str[2] == 'X': #lose: scissors(Z)
            return 0 + 3
        elif game_str[2] == 'Y': #tie: rock
            return 3 + 1
        else: #win, paper
            return 6 + 2
    elif game_str[0] == 'B': #paper
        if game_str[2] == 'X':  # lose, rock
            return 0 + 1  # loss + rock
        elif game_str[2] == 'Y':  # tie, paper
            return 3 + 2  # tie + paper
        else:
            return 6 + 3  # win + scissors
    else: #scissors
        if game_str[2] == 'X':  # lose, paper
            return 0 + 2
        elif game_str[2] == 'Y':  # tie, scissors
            return 3 + 3
        else:
            return 6 + 1  # win + rock

test_lst = ['A Y', 'B X', 'C Z']

total = 0

def test_game():
    total = 0
    for t in test_lst:
        print(points(t))
        total += part2(t)

    print("Total:",total)

test_game()
for game in lst:
    total += part2(game)
print("Total:",total)

print("Time (secs):",time.time()-starting_time)
