"""
Litovchenko Daniil

2 group 3 podgroup

"""

def mnoj(listarg):
    reslist=[*listarg[3][listarg[0]:listarg[1]+1:listarg[2]]]
    return reslist

def perem(lst):
    a = int(input("Введите начало диапазона: "))
    b = int(input("Введите конец диапазона: "))
    c = int(input("Введите шаг диапазона: "))
    listarg=[a, b, c, lst]
    return listarg

#############################
    
lst = [0, 1, 1, 2, 3, 5, 8, 13,
       21, 34, 55, 89, 144, 233,
       377, 610, 987, 1597, 2584,
       4181, 6765, 10946]

print("Необходимые элементы: ", *mnoj(perem(lst)))

#############################

#length = int(len(lst))


