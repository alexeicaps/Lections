# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8
#
# a = 3
# b = 5
# def f(a, b):
#     if b == 0:
#         return 1
#     return a * f(a, b - 1)
#
# print(f(a = 3, b = 5))


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# sum(2, 2)
# 4

# a = int(input("Type a number: "))
# b = int(input())
# def sum(a, b):
#     if b == 0:
#         return a
#     return 1 + sum(a, b - 1)
#
# print(sum(a, b))