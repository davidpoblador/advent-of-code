#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    seats = []
    for line in data.splitlines():
        row, col = line[0:7], line[-3:]
        rb = int(''.join([str(int(c == 'B')) for c in row]), 2)
        cb = int(''.join([str(int(c == 'R')) for c in col]), 2)
        seats.append(rb * 8 + cb)

    return max(seats)


def B():
    seats = []
    for line in data.splitlines():
        row, col = line[0:7], line[-3:]
        rb = int(''.join([str(int(c == 'B')) for c in row]), 2)
        cb = int(''.join([str(int(c == 'R')) for c in col]), 2)
        seats.append(rb * 8 + cb)

    i = min(seats)
    while i <= max(seats):
        if i not in seats:
            if i - 1 in seats and i + 1 in seats:
                return i
        i += 1


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
