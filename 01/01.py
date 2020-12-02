from itertools import combinations
from math import prod
from timeit import timeit

numbers = [int(x) for x in open('01.txt').readlines()]

def equal2020(haystack, matches):
    for nums in combinations(haystack, matches):
        if sum(nums) == 2020:
            return(prod(nums))

def part1():
    print(equal2020(numbers, 2))

def part2():
    print(equal2020(numbers, 3))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))
