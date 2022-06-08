"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""

def format_string():
    print(f"Hello, {name}")

my_list = ['alex', 'peter', 'koz', 'lyk', 'look']

for name in my_list:
    format_string()
