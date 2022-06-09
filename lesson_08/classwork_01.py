""""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода:
jump, run, bark. Каждый метод выводит сообщение на экран. Создать объект класса Dog,
вызвать все методы объекта и вывести на экран все его атрибуты.
"""

class dog:
    height = None
    weight = None
    name = None
    age = None

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        if age is nit None:
            self.age = age

    def jump(self):
        print(f{})

if __name__=="__main__":
    dog = dog(10, 5 ,5)
    print(dog.name)
