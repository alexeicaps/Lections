# Task 1
# Напишите функцию print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.


# print_operation_table(lambda x, y: x * y, 3, 3)
# num_rows = int(input("input number of rows: "))
# num_columns = int(input("input number of columns: "))

# def print_operation_table(operation, num_rows, num_columns):
#     if num_columns < 2 or num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' '.join([str(i) for i in range(1, num_rows + 1)]))
#         for i in range(2, num_rows + 1):
#             print(i, end=' ')
#             for j in range(2, num_columns + 1):
#                 print(operation(i, j), end=' ')
#             print()

# Эталонное решение -------------------------

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))


# print_operation_table(lambda x, y: x * y, 3, 3)
#
# print_operation_table(lambda x, y: x * y, 1, 2)
#
# print_operation_table(lambda x, y: x / y, 4, 4)
#
# print_operation_table(lambda x, y: x - y, 5, 5)
#
# print_operation_table(lambda x, y: x + y, 4, 4)

# def print_operation_table(operation, num_rows , num_columns ):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#     for i in range(2, num_rows + 1):
#         print(i, end = ' ')
#         for j in range(2, num_columns + 1):
#             print(operation(i, j), end = ' ')
#         print()

# print_operation_table(lambda x, y: x / y, 4, 4)

# print_operation_table(lambda x, y: x * y, 3, 3)
#
# print_operation_table(lambda x, y: x * y, 1, 2)
#
# print_operation_table(lambda x, y: x - y, 5, 5)

# print_operation_table(lambda x, y: x + y, 4, 4)

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 and num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' / '.join(str(i) for i in range(1, num_rows + 1)))
#     for i in range(2, num_rows + 1):
#         if num_rows:
#             print(i, end=" / ")
#         else:
#             print(i, end=' ')
#         for j in range(2, num_columns + 1):
#             if num_columns:
#                 print(operation(i, j), end=" / ")
#             else:
#                 print(j)
#         print()
#
# print_operation_table(lambda x, y: x + y, 4, 4)










# ////////////////////////////////////////////////////////////////////////

# задача с Винни-Пухом

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
#
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:
#   print('Количество фраз должно быть больше одной!')
# else:
#   countVowels = []
#
# for i in phrases:
#     countVowels.append(len([x for x in i if x.lower() in vowels]))
#
# if countVowels.count(countVowels[0]) == len(countVowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')



# Эталонное решение----------------------------------


line = input("input a phrase: ")
print(line)
lines = line.split()

print(lines)
if len(lines) < 2:
    print("Количество фраз должно быть больше одной!")
else:
    lst = [sum(x in 'уеыаоэяию' for x in lin) for lin in lines]
    # print(lst)
    if len(set(lst)) == 1:
        res = "Парам пам-пам"
    else:
        res = "Пам парам"
    print(res)


















# def rhythm(str):
#     str = str.split()
#     list = []
#     for word in str:
#         result = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 result += 1
#         list.append(result)
#     return len(list) == list.count(list[0])
#
# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# str = input()
# if rhythm(str):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

