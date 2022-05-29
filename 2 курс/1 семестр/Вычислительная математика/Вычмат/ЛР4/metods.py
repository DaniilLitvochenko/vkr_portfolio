from math import *

e = 10**(-6)

a = -10
b = 10


def func(x):
    return 2*x **3 - 9*x**2 - 60*x + 1


def proizv(x):
    return 6*x**2 - 18*x - 60


def newton():
    x0 = a
    xc = x0 - func(x0) / proizv(x0)
    while abs(xc - x0) >= e:
        x0 = xc
        xc = x0 - func(x0) / proizv(x0)
    print('x =', xc)


def chord():
    x0 = a
    xc = b
    if abs(x0) == abs(xc):
        xc += a/2
    while abs(xc - x0) >= e:
        x = xc - ((xc - x0) * func(xc)) / (func(xc) - func(x0))
        x0 = xc
        xc = x
    print('x =', xc)


def dichotomy():
    x0 = a
    xc = b
    if abs(xc) == abs(x0):
        xc += a/2
    x = (x0 + xc) / 2
    while abs(func(x)) > e:
        x = (x0 + xc) / 2
        if func(x0) * func(x) < 0:
            x0, xc = x0, x
        else:
            x0, xc = x, xc
    print('x =', (x0 + xc) / 2)
