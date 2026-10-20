import math

def f(x):
    return 1 / math.sqrt(x**2 + 2.5)
def simpson(a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)

    return (h / 3) * s


a = 1.6
b = 2.2
n = 10

result = simpson(a, b, n)

print("Результат:", result)