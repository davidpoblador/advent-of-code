#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():

    nice = 0
    for s in data.splitlines():
        if has3vowels(s) and hasduplicates(s) and notcontainssub(s):
            nice += 1

    return nice


def B():
    return 0
    from itertools import count
    from hashlib import md5

    for i in count(1):
        to_hash = "{}{}".format(data, i).encode('utf-8')
        if md5(to_hash).hexdigest().startswith('000000'):
            return i


def notcontainssub(s):
    for ss in ('ab', 'cd', 'pq', 'xy'):
        if ss in s:
            return False
    return True


def has3vowels(s):
    v = 'aeiou'

    c = sum([s.count(c) for c in v])

    return c >= 3


def hasduplicates(s):
    from itertools import groupby
    r = [i[0] for i in groupby(s)]

    return (len(s) != len(r))


def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
