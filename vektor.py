import numpy as np
import math
#############
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# c = []
#
# for i in range(len(a)):
#     c.append(a[i] + b[i])
#
# print("Сумма векторов:", c)

################
# a = [2, 3, 4]
# k = 3
#
# result = []
#
# for i in range(len(a)):
#     result.append(a[i] * k)
#
# print("Результат:", result)

#
# #################
#
# import math
#
# a = [3, 4]
#
# s = 0
#
# for x in a:
#     s += x ** 2
#
# result = math.sqrt(s)
#
# print("Модуль вектора:", result)
#
# #####################
#
#

#
# a = [1, 0]
# b = [0, 1]
#
# dot = 0
# sum_a = 0
# sum_b = 0
#
# for i in range(len(a)):
#     dot += a[i] * b[i]
#     sum_a += a[i] ** 2
#     sum_b += b[i] ** 2
#
# cos_angle = dot / (math.sqrt(sum_a) * math.sqrt(sum_b))
#
# angle = math.degrees(math.acos(cos_angle))
#
# print("Угол между векторами:", angle, "градусов")

# ############
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# result = 0
#
# for i in range(len(a)):
#     result += a[i] * b[i]
#
# print("Скалярное произведение:", result)

# ########################
#
#
# a = np.array([1, 0, 0])
# b = np.array([0, 1, 0])
# c = np.array([0, 0, 1])
#
# vector_product = np.cross(a, b)
#
# print("Векторное произведение:", vector_product)
# mixed_product = np.dot(vector_product, c)
# print("Смешанное произведение:", mixed_product)