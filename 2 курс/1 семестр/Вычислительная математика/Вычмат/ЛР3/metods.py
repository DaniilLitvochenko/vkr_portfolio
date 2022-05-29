from math import *

def logarithm(arr):
    x = 0.5
    n = 1
    summa = 0
    while n <= 4:
        f = arr[n] * x ** n
        summa += f
        n += 1
    print("ln(1 + x) = ", summa)
    print("При x = ", x)

def arctan(arr):
    x = pi / 6
    n = 0
    summa = 0
    while n <= 10:
        f = arr[n] * x ** (2 * n + 1)
        summa += f
        n += 1
    print("arctg x = ", summa)
    print("При x = ", x)

def cheb_exp(arr):
    x = 0.5
    summa = 0
    for i in range(len(arr)):
        summa += arr[i] * x ** i
    print("exp x = ", summa)
    print("При x = ", x)


def cheb_sin(arr):
    x = pi / 6
    summa = 0
    for i in range(len(arr)):
        summa += arr[i] * x**(i*2+1)
    print("sin x = ", summa)
    print("При x = ", x)

