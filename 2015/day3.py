#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    pairs = set()
    x, y = 0, 0

    for c in data:
        pairs.add((x, y,))
        if c == '>':
            x += 1
        elif c == '<':
            x -= 1
        elif c == '^':
            y -= 1
        elif c == 'v':
            y += 1
        else:
            raise Exception

    return len(pairs)


def B():
    pairs = set()

    pos = [[0, 0], [0, 0]]
    pairs.add((0, 0, ))

    for i, c in enumerate(data):
        if c == '>':
            pos[i % 2][0] += 1
        elif c == '<':
            pos[i % 2][0] -= 1
        elif c == '^':
            pos[i % 2][1] -= 1
        elif c == 'v':
            pos[i % 2][1] += 1
        else:
            raise Exception

        pairs.add(tuple(pos[i % 2]))

    return len(pairs)


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
