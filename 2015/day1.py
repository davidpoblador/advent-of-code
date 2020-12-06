#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    s = 0
    for c in data:
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1

    return s


def B():
    s = 0
    p = 0
    for c in data:
        p += 1
        if c == '(':
            s += 1
        elif c == ')':
            s -= 1

        if s < 0:
            return p


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
