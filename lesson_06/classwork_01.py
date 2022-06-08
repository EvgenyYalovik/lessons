"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский,
где слово - это входной параметр, вторая функция - с русского на английский.
"""

my_dict = {
    "apple": "яблоко",
    "green": "зеленный",
    "fly": "летать",
}

def end_to_rus(word):
    return my_dict[word]


def rus_to_end(word):
    for key, value in my_dict.items():
        if value == word:
            return key


print(end_to_rus("apple"))
print(end_to_rus("fly"))