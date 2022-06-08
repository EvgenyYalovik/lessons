"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается, достать ли следующую карту,
в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

from classwork_02 import get_random_card

my_dict = {"6":6, "7":7, "8":8, "9":9, "10":10, "j":2, "q":3, "k":4, "a":1
           }


def nom_to_value(nominal):
    return my_dict[nomial]

n, m = get_random_card()
value = nominal_to_value(n)


current_sum = value

while True:
    choice = input("достать следующую карту [y/n]: ")
    if choice == "n":
        break


    n, m = get_random_card()
    value = nominal_to_value(n)
    current_sm += value

    if current_sum > 21:
        print ("game over")
        break

    if current_sum == 21:
        print ("win")
        break

    if current_sum < 21:
        print ("текущая сумма: ", current_sum)
