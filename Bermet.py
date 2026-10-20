# import math
#
# def f(x):
#     return 1 / math.sqrt(x**2 + 2.5)
#
# def simpson(a, b, n):
#     h = (b - a) / n
#
#     print(" i       x          f(x)        Коэффициент")
#     print("---------------------------------------------")
#
#     s = f(a) + f(b)
#
#     print(f" 0     {a:.2f}     {f(a):.6f}          1")
#
#     for i in range(1, n):
#         x = a + i * h
#
#         if i % 2 == 0:
#             k = 2
#             s += 2 * f(x)
#         else:
#             k = 4
#             s += 4 * f(x)
#
#         print(f"{i:2d}     {x:.2f}     {f(x):.6f}          {k}")
#
#     print(f"{n:2d}     {b:.2f}     {f(b):.6f}          1")
#
#     return (h / 3) * s
#
#
# a = 1.6
# b = 2.2
# n = 18
#
# result = simpson(a, b, n)
#
# print("---------------------------------------------")
# print(f"Результат: {result:.6f}")


import math

def f(x):
    return math.log10(x**2 + 1) / x

a = 0.8
b = 1.6
n = 10

h = (b - a) / n

print(" i      x          f(x)        k*f(x)")
print("-----------------------------------------")

s = 0

for i in range(n + 1):
    x = a + i * h
    y = f(x)

    if i == 0 or i == n:
        k = 1
    elif i % 2 == 1:
        k = 4
    else:
        k = 2

    s += k * y

    print(f"{i:2d}   {x:.2f}      {y:.6f}      {k*y:.6f}")

result = (h / 3) * s

print("-----------------------------------------")
print("h =", h)
print(f"Результат = {result:.6f}")