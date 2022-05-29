import metods

def printmain():
    for i in range(5):
        print(mainlist[i])
    print()

def printchangelist():
    for i in range(6):
        print(changelist[i])
    print()

def printpostlist():
    for i in range(4):
        print(postlist[i])
    print()

def readlist():
    print("Введите значения a, b, n: ")
    a=float(input("a = "))
    b=float(input("b = "))
    n=int(input("n = "))
    listarg=[a, b, n]
    return listarg

def readlist2():
    print("Введите значения a, b, E: ")
    a=float(input("a = "))
    b=float(input("b = "))
    e=float(input("E = "))
    listarg=[a, b, e]
    return listarg

def readlist3():
    print("Введите значения a, b, c, d, nx, ny: ")
    print("Введите первую область интегрирования:")
    a=float(input("a = "))
    b=float(input("b = "))
    print("Введите вторую область интегрирования:")
    c=float(input("c = "))
    d=float(input("d = "))
    print("Введите количество разбиений:")
    nx=int(input("nx = "))
    ny=int(input("ny = "))
    listarg=[a, b, c, d, nx, ny]
    return listarg
    
    

mainlist=["Главное меню", "1) Методы с постоянным шагом",
          "2) Методы с переменным шагом", "3) Двойной интеграл","4) Выход из программы"]

changelist=["Методы с постоянным шагом", "1) Метод правых частей прямоугольников",
            "2) Метод левых частей прямоугольников", "3) Метод трапеций",
            "4) Метод парабол", "5) Возврат в главное меню"]

postlist=["Методы с переменным шагом", "1) Метод по 1 алгоритму",
          "2) Метод по 2 алгоритму", "3) Возврат в главное меню"]

while True:
    printmain()
    switch=int(input())
    if switch==1:
        while True:
            printchangelist()
            switch1=int(input())
            if switch1==1:
                print("Результат: ", metods.pryamr(readlist()))
            elif switch1==2:
                print("Результат: ", metods.pryaml(readlist()))
            elif switch1==3:
                print("Результат: ", metods.trap(readlist()))
            elif switch1==4:
                print("Результат: ", metods.par(readlist()))
            elif switch1==5:
                break    
    elif switch==2:
        while True:
            printpostlist()
            switch2=int(input())
            if switch2==1:
                print("Результат: ", metods.met1(readlist2()))
            elif switch2==2:
                print("Результат: ", metods.met2(readlist2()))
            elif switch2==3:
                break      
    elif switch==3:
        print("Результат: ",metods.double_integral(readlist3()))
    elif switch==4:
        break
    
    
print("Программа завершена")

