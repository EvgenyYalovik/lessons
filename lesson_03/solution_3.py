"""
Создать список, который состоит из отдельных единичных символов.
Преобразовать список в строку, инвертировать строку и вывести на печать.
"""

my_list = ["a", "p", "p", "l", "e"]

print("New string:", "_".join(my_list)[::-1])    # New string: e_l_p_p_a