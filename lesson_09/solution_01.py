"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение
площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.

"""

from __future__ import annotations
from math import pi, sqrt


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def square(self) -> float:
        return (pi * self.radius) ** 2