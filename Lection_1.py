# Объявление списков

# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(list_1)
# print(*list_1)


# Добавление элемента в список

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# Удаление элемента из списка

# print(list_1.pop(0))
# print(list_1)


# Срезы в списках

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])                # 1
# print(list_1[-5])               # 6
# print(list_1[:])                # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[len(list_1)-2:])   # [9, 10]
# print(list_[0:len(list_1):6])   # [1, 7]
# print(list_1[::6])              # [1, 7]



# -------------------------------------КОРТЕЖИ -----------------------------------

# Кортеж - это неизменяемый список

# t = ()
# print(type(t))     # <class 'tuple'>
#
# t = (1)
# print(type(t))     # <class 'int'>
#
# t = (1, )          # если вставляем значения, то обязательно запятую в конце, чтобы объявить кортеж
# print(type(t))     # <class 'tuple'>

# v = [1, 8, 9]        # объявили список
# print(v)
# print(type(v))       # <class 'list'>
#
# v = tuple(v)         # преобразовали список в кортеж
# print(v)
# print(type(v))       # <class 'tuple'>
#
#
# a, b, c = v
# print(a, b, c)       # сделали распаковку кортежа по элементам

# t = (1, 2, 3, 5, )
#
# print(t[1])            # выводим элемент кортежа
#
# for i in t:
#     print(i)           # 1 2 3 5 (data output in column)
#
# for i in range(len(t)):  # the same output with function 'range'
#     print(t[i])        # 1 2 3 5 (data output in column)


t = (1, 2, 3, 5, )
t[0] = 2
print(t)                 # TypeError: 'tuple' object does not support item assignment