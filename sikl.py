# for i in range(1, 21):
#     print(i)
###########
# total = 0
#
# for i in range(1, 101):
#     total += i
#
# print("Сумма:", total)
################
# text = input("Введите строку: ")
# count = 0
# for letter in text:
#     if letter.lower() == "а":
#         count += 1
# print("Количество букв а:", count)
###############
# n = int(input("Введите целое число: "))
#
# for i in range(1, 11):
#     print(n, "*", i, "=", n * i)
############
# numbers = [45, 12, 89, 33, 56, 3439,99, 2]
# maximum = numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum = number
#
# print("Максимальное число:", maximum)
##################
# n = int(input("Введите натуральное число: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print("Факториал:", factorial)

##################
# import random
# numbers = [random.randint(1, 100) for i in range(10)]
# print("Список:", numbers)
#
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

####################
# n = int(input("Введите количество чисел: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#############
# n = int(input("Введите целое число больше 1: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("Число не простое")
#         break
# else:
#     print("Число простое")

#################
# n = int(input("Введите высоту треугольника: "))
#
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()

##############2222222222222##################3
# for i in range(10, 0, -1):
#     print(i)
# print("Старт!")

################
# i = 2
# while i <= 20:
#     print(i)
#     i += 2

####################
# for i in range(1, 11):
#     print(i ** 2)

################33
# while True:
#     word = input("Введите слово: ")
#
#     if word == "стоп":
#         break
#
#     print(word)

#################
# password = ""
#
# while password != "admin":
#     password = input("Введите пароль: ")
#
# print("Пароль правильный!")

##################
# while True:
#     word = input("Введите слово: ")
#
#     print("Длина слова:", len(word))
#
#     if len(word) < 3:
#         break

#######################
# total = 0
# while True:
#     number = int(input("Введите число: "))
#     if number == 0:
#         break
#     total += number
# print("Итоговая сумма:", total)

#######################
# total = 0
#
# while total < 5000:
#     money = float(input("Сколько отложили сегодня? "))
#     total += money
#     print("В копилке:", total)
#
# print("Ура, накопили!")

#############
# number = 1
#
# while number <= 1000:
#     number *= 2
#     print(number)
#############3
# number = 100
#
# while number > 1:
#     number /= 2
#     print(number)
