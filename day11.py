# Advent of Code 2022 Day 11
# https://adventofcode.com/2022/day/11

import time

starting_time = time.time()

lst = [l.strip() for l in open('day11.txt')]
#lst = [l.strip() for l in open('day11_test.txt')]

class Monkey(object):
    def __init__(self,num):
        """num: assigned number
        items: starting items
        opn: operation, like "* 5"
        test [n,t,f]: divisibility by n and monkeys it
           throws to if True or False"""
        self.num = num
        self.items = list()
        self.opn = list()
        self.tst = list()
        self.inspected = 0

    def operate(self):
        pass

    def test(self,level,lcm):
        level %= lcm
        #print("monkey",self.num)
        #print("level in:",level)
        if self.num == 7:
            level *= level
        else:
            if self.opn[0]=='*':
                level *= int(self.opn[1])
            elif self.opn[0]=='+':
                level += int(self.opn[1])
        #divide level by 3, round down
        #level = level // 3 #not in part 2
        #print("level out:",level)
        #print("Divisible by",self.tst[0],'?')
        if level % self.tst[0] == 0:
            monkeylst[self.tst[1]].items.append(level)
            #print("Yes. To monkey",monkeylst[self.tst[1]].num)
        else:
            monkeylst[self.tst[2]].items.append(level)
            #print("No. To monkey", monkeylst[self.tst[2]].num)
    def round(self,lcm):
        #print("monkey", self.num, "items:", self.items)
        newlist = list()
        for level in self.items:
            self.test(level,lcm)
            self.inspected += 1
        self.items = newlist[::]

monkeylst = list()

def part1():
    #get monkeys set up, into list
    divisors = list()
    for i in range(8):
        monkeylst.append(Monkey(i))
        #print(lst[(8 * i):(8 * (i + 1))])
        for j in range(7):
            if j == 0:
                continue
            if j == 1:
                items = lst[7*i+1].split(':')[1]
                items = [int(x) for x in items.split(',')]
                #print(items)
                # for t in items:
                #     print(t,type(t))
                monkeylst[i].items = [int(x) for x in items]
                #print(items)
            if j == 2:
                oplist = lst[7*i+2].split(" ")[-2:]
                monkeylst[i].opn = oplist
            if j == 3:
                monkeylst[i].tst = list()
                test_list = lst[7*i+3].split(' ')
                monkeylst[i].tst.append(int(test_list[-1]))
                divisors.append(int(test_list[-1]))
            if j == 4:
                monkeylst[i].tst.append(int(lst[7*i+4].split(' ')[-1]))
            if j == 5:
                monkeylst[i].tst.append(int(lst[7*i+5].split(' ')[-1]))
        #print("Monkey",i,":",monkeylst[i].tst)
    lcm = 1
    for d in divisors:
        lcm *= d
    for i in range(10000):
        for m in monkeylst:
            m.round(lcm)
        #print("Round:",i+1)
        # for m in monkeylst:
        #     print(m.items)

    for m in monkeylst:
        print(m.inspected)


part1() #First try 9600, too low --> 50172 correct

print("Time (secs):",time.time()-starting_time)
