#!/usr/bin/env python

from pprint import pprint
from aocd import AocdError

try:
    from aocd import data, submit
except AocdError:
    exit("Something is not right (probably missing day)")


def A():
    from itertools import count
    from hashlib import md5

    for i in count(1):
        to_hash = "{}{}".format(data, i).encode('utf-8')
        if md5(to_hash).hexdigest().startswith('00000'):
            return i

def B():
    from itertools import count
    from hashlib import md5

    for i in count(1):
        to_hash = "{}{}".format(data, i).encode('utf-8')
        if md5(to_hash).hexdigest().startswith('000000'):
            return i

def print_solutions():
    for part in ['A', 'B']:
        print("PART {}:".format(part), globals()[part]())


if __name__ == "__main__":
    print_solutions()
