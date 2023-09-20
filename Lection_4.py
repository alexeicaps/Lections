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

n = int(input("Введите первое множество n: "))
m = int(input("Введите первое множество m: "))
list_1 = set()
list_2 = set()

for i in list_1:
    # x = int(input("Введите элемент множества n: "))
    list_1.add(int(input("Введите элемент множества n: ")))
print(list_1)

for j in list_2:
    y = int(input("Введите элемент множества n: "))
    list_1.add(y[0])
print(result)
max_number = 0






# list_1 = {1, 2, 33, 45, 95, 4, 5}
# list_2 = {6, 5, 9, 45, 59, 14, 54}
# b = list_1.union(list_2)
# print(b)