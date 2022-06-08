"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так,
чтобы они не били друг друга (ферзь может ходить по горизонтали, вертикали и диагонали).
Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

"""

def is_figures_beat_each_other(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


def main():
    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))
    if is_figures_beat_each_other(x1, y1, x2, y2):
            print("Yes")
    else:
            print("No")

    if __name__ == "__main__":
        main()