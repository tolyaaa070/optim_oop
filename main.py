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
м
print("-----------------------------------------")
print("h =", h)
print(f"Результат = {result:.6f}")