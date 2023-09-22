# data_example = {22, 11, 2, 3, 5}
# print(data_example)
# data_example.add(2)
# print(data_example)
# data_example.add(3)
# data_example.add(23)
# print(data_example)
# data_example.add(11)
# print(data_example)
# data_example.add(101)
# print(data_example)
# data_example.add(1.01)
# print(data_example)
# data_example.add(True)
# print(data_example)

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# str1 = 'a a a b c a a d c d d'
# print(str1)
# str1 = str1.split()
# my_dict = {}
#
# for i in str1:
#     if i not in my_dict:
#         my_dict[i] = 0
#         print(i, end = " ")
#     else:
#         my_dict[i] += 1
#         print(f'{i}_{my_dict[i]}', end=' ')


# Task 27 --------------------------------------------------------------------------------------------------------
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# str_1 = '''She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower()
# print(str_1)
# str_1 = set(str_1.split())
# print(len(str_1))

# V_2
# print(set(input("Input text: ").lower().split()))



# ------DEBUG----------------------------------------------

# n = int(input("Введите число: "))
# max_number = n
# while n != 0:
#    n = int(input("Введите число: "))
#    if max_number < n:
#        max_number = n
# print(max_number)

# a = len("agrfdfb sdjnf adfjvbnd dfvg df dfg df sdf vsdfb sfgb asdfv".split())
# print(a)


# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n = int(input("Введите первое множество n: "))
# m = int(input("Введите первое множество m: "))
# list_1 = set()
# list_2 = set()
# for i in range(list_1[n]):
#     x = int(input("Введите элемент множества n: "))
#     print(i)
#

# list_3 = list_1.intersection(list_2)
# print(list_3)



# list_44 = {5, 3, 29, 4, 1, 6, 84}
# list_44.add(25)
# print(list(list_44))

# a = {1, 3, 6, 4, 8, 25}
# print(a)
# a.add(11)
# print(a)
# a.update({26, 29, 28})
# print(a)
# a.discard(4)
# print(a)
# a.remove(28)
# print(a)
# a.discard(28)
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)

# a = {1, 3, 6, 4, 8, 25, 8}
# print(len(a))
# print(8 in a)
# print(33 in a, 7 in a, 7 not in a)

# a = {1, 3, 6, 4, 8, 25, 8}
# b = {1, 65, 6, 2, 8, 25, 9}
# g = {2, 3, 6, 9, 15}
# h = {15, 9, 2, 3, 6}
# c = a.union(b)
# d = a.intersection(b)
# print(c)
# print(d)
# print(a.intersection(g, b))
# print(a | b)
# print(a - g)
# print(g == h)

# list2 = [1, 2, 3]
# print(list2)
# print(set(list2), type(list2))
# a = set(list2)
# print(a, type(a))

# list5 = {5, 3, 6, 4, 9}
# print(list5)
# b = list(list5)
# print(b, type(b))

# list5 = {5, 3, 6, 4, 9}
# t = tuple(list5)
# print(t, type(t))
# l = list(t)
# print(l, type(l))
# for i in list5:
#     print(i)

text = input()
a = set()
while text != ' ':
    slova = text.split()
    a.update(slova)
    print(a)
    text = input()

