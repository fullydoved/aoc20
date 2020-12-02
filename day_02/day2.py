from timeit import timeit
import re

lines = open('day2.txt').readlines()

def part1():
    valid = 0
    for line in lines:
        pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
        low_range, high_range, needle, haystack = pattern.findall(line)[0]
        if haystack.count(needle) >= int(low_range) and haystack.count(needle) <= int(high_range):
            valid += 1
    print("{} valid passwords found.".format(valid))

def part2():
    valid = 0
    for line in lines:
        pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
        low_range, high_range, needle, haystack = pattern.findall(line)[0]
        if (haystack[int(low_range)-1] == needle and haystack[int(high_range)-1] != needle) or (haystack[int(low_range)-1] != needle and haystack[int(high_range)-1] == needle):
            valid += 1
    print("{} valid passwords found.".format(valid))

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))
