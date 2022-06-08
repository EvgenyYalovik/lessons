"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал
(6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random

n = ("6", "7", "8", "9", "10", "j", "q", "k", "a")
m = ("h", "d", "c", "s")


def get_random_card():
    random_n = random.choice(n)
    random_m = random.choice(m)
    return random_m, random_n

for _ in range(5):
    print(get_random_card())
