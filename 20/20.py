from timeit import timeit

lines = open('03.txt').readlines()
# numbers = [int(x) for x in open('03.txt').readlines()]

def part1():
    pass

def part2():
    pass

if __name__ == '__main__':
    print("Part 1: ", end="")
    print("time: ", timeit(part1, number=1))
    print("Part 2: ", end="")
    print("Time: ", timeit(part2, number=1))
