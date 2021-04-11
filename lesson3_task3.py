# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func():
    arg1 = float(input('Введите первое число: '))
    arg2 = float(input('Введите второе число: '))
    arg3 = float(input('Введите третье число: '))
    if arg1 >= arg3 and arg2 >= arg3:
        return print(arg1 + arg2)
    elif arg1 > arg2 and arg1 < arg3:
        return print(arg1 + arg3)
    else:
        return print(arg2 + arg3)
my_func()