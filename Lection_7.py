# -------------------------///////////---------------- ЛЕКЦИЯ 4 ------------------//////////////------------------------
#
# Урок 4. Функции высшего порядка, работа с файлами

# def f(x):
#     return x * x
#
# a = f
#
# print(a(5))
# print(f(5))

# -----------------------

# def calk1(a, b):
#     return a + b
#
# def math(op, x, y):
    # return(op, x, y)

# calk1 = lambda a,b: a + b

# math(lambda a,b: a + b, 5, 45)

# -----------------------------
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).

# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in list_1:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
#
# print(res)






# # def select(f, col):
# #     return [f(x) for x in col]
# #
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38, 56, 22]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
#
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# ------------------------------------------------function 'MAP'--------------------------------------------------------

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# -------------------

# data = '15 156 96 3 5 8 52 5'
# print(data)

# data = data.split()
# print(data)
#
# res = list(map(int, data))
# print(res)

# data = list(map(int, data.split()))
# print(data)

# ----------------------------------------------function 'FILTER'-------------------------------------------------------


# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

#
# data = [1, 2, 3, 5, 8, 15, 23, 38, 56, 22]
# res = list(map(int, data))
# print(res)
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)


# -----------------------------------------------function 'ZIP'---------------------------------------------------------

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 17, 7]
# res = list(zip(users, ids))
# print(res)
#
# salary = [111, 256, 325]
# res2 = list(zip(users, ids, salary))
# print(res2)


# -----------------------------------------------function 'ENUMERATE'---------------------------------------------------

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# res = list(enumerate(users))
# print(res)
#
# data = ('a', 'b', 'c', 'd')
# a_data = list(enumerate(data))
# print(a_data)

# my_dict = {'a': 151, 'b': 221, 'c': 315, 'd': 625, 'e': 758}
# a_dict = list(enumerate(my_dict))
# print(a_dict)

# ---------------------------------------------work with files----------------------------------------------------------

# users = ['red', 'blue', 'pink', 'grey', 'brown']
# my_file = open('text.txt', 'a')
# my_file.writelines(users)
# my_file.close()

# with open('file.txt', 'w') as my_file:
#     my_file.write('line 1\n')
#     my_file.write('line 2\n')
# print(56)

# with open('text.txt', 'w') as my_file:
#     my_file.write('line 1\n')
#     my_file.write('line 2\n')
# print(56)

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()








# trasformation = lambda x: x
#
# values = [1, 23, 42, 'asdf']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# ///////////////////////////////////////////////
# Задача №49.

# print(1!= 2)

# def find_farthest_orbit(orbits):
#     condition = lambda data: (data[0] != data[1]) * data[0] * data[1]
#     square_orbits = list(map(condition, orbits))
#     return orbits[square_orbits.index(max(square_orbits))]
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# //////////////////////////////////////////////////////////////////////////////////////

# a = [100, 33, 90, 54, 3, 9]
# def max_a(a):
#     res = list(filter(int, a))
#     return a.index(max(res))
#
# print(max_a(a))
#
# def min_a(a):
#     res = list(filter(int, a))
#     return a.index(min(res))
#
# print(min_a(a))


# ///////////////////////////////////////////////
# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:                                                   Вывод:
# values = [0, 2, 10, 6]                                  same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     # print(set(map(characteristic, objects)))
#     return len(set(map(characteristic, objects))) in (0, 1)
#
#
# values = [35, 13, 15, 17]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')




# , sep='\n')

