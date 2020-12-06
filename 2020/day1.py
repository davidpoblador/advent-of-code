#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    nums = []
    for line in data.splitlines():
        i = int(line)
        if i >= 2020:
            continue

        if not len(nums):
            nums.append(i)
            continue

        for n in nums:
            if i + n == 2020:
                return n*i

        nums.append(i)


def B():
    nums = []
    for line in data.splitlines():
        i = int(line)
        if i >= 2020:
            continue

        if len(nums) < 2:
            nums.append(i)
            continue

        for x in nums:
            for y in nums:
                if i + x + y == 2020:
                    return i * x * y

        nums.append(i)


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
