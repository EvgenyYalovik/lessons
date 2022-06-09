
"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости).
"""

class Car:
    brand = ''
    model = ''
    year = " "
    speed = 0

    def speedup(self):
        self.speed +=5
    def slowdown(self):
        self.speed -=5
    def stop(self):
        self.speed = 0
    def logspead(self):
        print(self.speed)
    def reverse(self):
        speed = -speed

