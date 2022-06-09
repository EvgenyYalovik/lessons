"""
Написать функцию, которая будет вызывать задержку выполнения программы случайным образом от 1-й до 5-ти секунд.
Написать декоратор, который будет выводить на печать время выполнения этой функции (end_time - start_time).
"""


class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self):
        self.start_pt = (10, 5)
        self.end_pt = (100, 20)
        self.color = 'blue'


fig1 = Figure()
delattr(fig1, "color")

for key in fig1.__dict__.keys():
    print(key, end=' ')
