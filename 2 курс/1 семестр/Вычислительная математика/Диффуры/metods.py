from math import *

def func(x, y):
    return y*(1-x)


def eler(a, b, n, x, y):
    h=(b-a)/n
    print("Шаг: ", h)
    while x<=b-h:
        print("x =", round(x, 1), "y =", y)
        y += h * func(x, y)
        x += h


def ruku(a, b, n, x, y):
    def ruchange(x, y, h):
        res=[]
        res.append(h*func(x, y))
        res.append(2*h*func(x+h/2, y+res[0]/2))
        res.append(2*h*func(x+h/2, y+res[1]/2))
        res.append(h*func(x+h, y+res[2]))
        return sum(res)/6

    h=(b-a)/n
    while x<=b-h:
        print("x =", round(x, 1), "y =", y)
        y+=ruchange(x, y, h)
        x+=h


def vtor(a, b, h, y, z):
    x=a
    while x<b:
        y1=y
        print("x =", round(x, 5), "y =", round(y, 5), "z =", round(z, 5))
        y+=h*z
        z-=h*(z/x+y1)
        x+=h


def sistema(a, b, h, x, y, z):
    t=a
    while t<b:
        print("x =", round(x, 5),
              "y =", round(y, 5),
              "z =", round(z, 5),
              "t =", round(t, 5))
        x0=x
        y0=y
        z0=z
        x+=h*(-2*x0+5*z0)
        y+=h*(sin(t-1)*x0-y0+3*z0)
        z+=h*(-x0+2*z0)
        t+=h
