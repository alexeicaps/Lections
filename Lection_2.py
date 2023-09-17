# 1. Создать список чисел от 1 до 100

# list_1 = []
# for i in range(1, 101 ):
#     list_1.append(i)
# print(list_1)

# эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)]
print(list_1)

# 2. Добавить условия (только чётные числа)

list_1 = [ i for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Допустим вы решили создать пары каждому из чисел (кортежи)

list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. Например умножить значение на два.

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)