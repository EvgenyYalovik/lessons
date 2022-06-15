
from math import floor, sqrt

inputs = [12, 127, 332, 982, 4372, 11467]

def solve(x):
    result = []
    while(x > 0):
        max_panel_square = floor(sqrt(x)) ** 2
        print(max_panel_square)
        x -= max_panel_square
        result.append(max_panel_square)
    return result

for i in inputs:
    solve(i)
