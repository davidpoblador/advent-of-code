#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError
from math import prod

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    area = 0
    for dims in data.splitlines():
        a, b, c = [int(d) for d in dims.split('x')]
        faces = [a*b, b*c, a*c]
        area += (2 * sum(faces)) + min(faces)

    return area


def B():
    ribbon = 0
    for dims in data.splitlines():
        lens = [int(d) for d in dims.split('x')]
        wrap = 2 * (sum(lens) - max(lens))
        bow = prod(lens)

        ribbon += bow + wrap

    return ribbon


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
