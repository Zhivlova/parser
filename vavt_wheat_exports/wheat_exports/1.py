from cmath import sqrt


def func(x):
    if (x) ** 2 < 0.000001:
        solution = True
    else:
        solution = False
    return solution


print(func(-44.55))
print((-44.55) ** 2)
