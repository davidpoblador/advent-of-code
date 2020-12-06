#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    ans = 0
    for group in data.split("\n\n"):
        s = set()
        for line in group.split():
            for c in line:
                s.add(c)

        ans += len(s)

    return ans


def B():
    from collections import Counter
    ans = 0
    for group in data.split("\n\n"):
        q = Counter()
        e = 0
        for line in group.split():
            e += 1
            for c in line:
                q[c] += 1

        for v in q.values():
            if v == e:
                ans += 1

    return ans


solutions = [None, None]


def print_solutions():
    for i, part in enumerate(['A', 'B']):
        solution = globals()[part]()
        if solutions[i] is not None:
            assert (solution == solutions[i])

        print("PART {}:".format(part), solution)


if __name__ == "__main__":
    print_solutions()
