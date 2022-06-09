"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""


class Animal:
    height: int = None
    weight: int = None
    name: str = None
    age: int = 10

    def __init__(self, *args, **kwargs):
        self.height = kwargs.get("height")
        self.weight = kwargs.get("weight")
        self.name = kwargs.get("name")
        if kwargs.get("age") is not None:
            self.age = kwargs.get("age")

    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print(f"{self.name} is barking.")


if __name__ == "__main__":
    dog1 = Dog(height=10, weight=5, name="First")
    dog1.jump()

    dog2 = Dog(height=10, weight=5, name="Second", age=5)
    dog2.talk()
"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog1 = NewDog(height=10, weight=5, name="First name")
    print("Old name: ", dog1.name)
    dog1.change_name("New name")
    print("New name: ", dog1.name)

