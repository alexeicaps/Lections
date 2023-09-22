# Task 20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;


# word = input("Input word: ").upper()
# data = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1,
#         "D, G, Д, К, Л, М, П, У": 2,
#         'B, C, M, P, Б, Г, Ё, Ь, Я': 3
#         'F, H, V, W, Y, Й, Ы': 4
#         'K, Ж, З, Х, Ц, Ч': 5
#         'J, X, }
# result = 0
# for char in word:
#     for key in data:    # data.keys()    "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т" (first key, after one itteration)
#         if char in data:
#             result += data[key]
# print(result)



# print(*[chr(i) for i in range(ord('a'), ord('z') + 1)]) вывод английского алфавита

# print('hel' in 'hello')


# Task 31
# Fibonacci






# Task 33

# n = int(input("Input count marks: "))
# marks = [int(i) for i in input("Input marks: ").split()[:n]]
# print(*[min(marks) if i == max(marks) else i for i in marks])


# Task 35

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# print('yes' if is_prime(int(input("Input number: "))) else 'no')


# Task 37

# def rec(n):
#     if n == 0:
#         return ''
#     x = int(input("Введите число: "))
#     return rec(n - 1) + f' {x}'
#
#
# n = int(input("Введите кол-во чисел: "))
# print(rec(n))
# # rec(2) -> x = 3 -> rec(1) + ' 3' = " 4" + " 3"
# #                      |
# #                    rec(0) + ' 4' = '' + " 4"
# #                      |
# #

# Task 26