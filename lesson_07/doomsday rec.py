from functools import reduce
from math import floor, sqrt

inputs = [100000, 12, 7, 1]

def get_max_square(s):
    return floor(sqrt(s)) ** 2

def solve(x):
    result = []
    while(x > 0):
        s = get_max_square(x)
        x -= s
        result.append(s)
    return result

def solve_rec(x, result):
    s = get_max_square(x)
    if (x > 0):
        result.append(s)
        return solve_rec(x - s, result)
    else:
        return result