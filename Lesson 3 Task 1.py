"""Homework 3 Task 1

    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

    """
a=1
def first_func(var_1, var_2):
    if var_2==0.0:
        return "division by zero"
    return var_1/var_2

num = float(input("NUM: "))
denom = float(input("DENOM: "))
print(first_func(num, denom))

