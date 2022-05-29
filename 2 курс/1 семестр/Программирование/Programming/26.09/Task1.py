import math

def discr(b, a, c):
    """
Вычисление дискриминанта
    """
    #docstring
    return b*b-4*a*c

#упаковка
def sup_dis(*args):
    print(type(args))

discr(*(1,2,3))#распаковка
# print(dis(b=1),(a=3),(c=10))


#a=int(input("Введите a: "))
#b=int(input("Введите b: "))
#c=int(input("Введите c: "))
a=4
b=5
c=-1

print(discr(b,a,c))
print(discr.__doc__)

#help(len)

def sup_dis(*args):
    print(args)

discr(*[1,2,3])#распаковка
print(type(sup_dis(1,2,3)))


def sup_sup_dis(a=None, b=None, c=None):
    print(a,b,c)

sup_sup_dis(**({'a':1,'b':2,'c':3}))

def sup_sup_dis2(**kwargs):
    print(kwargs)
sup_sup_dis2(a=1,b=2,c=3,nick='i debil')