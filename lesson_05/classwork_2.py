"""
Создать функцию, которая принимает на вход неопределенное
количество аргументов и возвращает их сумму и максимальное из них.
"""
def sun_and_max( ):
    result_sum=0
    max_item=0
    for item in args:
        result_sum +=item

        if item > max_item:
            max_item = item
    return result_sum, max_item
my_list=(1, 2, 5, 19, 123, 22)
print(sum_and_max(*my_list))
print(sum_and_max(1, 2, 5, 19, 123, 22))
