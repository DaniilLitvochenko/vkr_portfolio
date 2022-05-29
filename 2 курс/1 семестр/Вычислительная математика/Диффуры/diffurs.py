import metods

def printmain():
    for i in range(5):
        print(mainlist[i])
    print()

def printchangelist():
    for i in range(4):
        print(changelist[i])
    print()
    
mainlist=["Главное меню", "1) Решение ДУ",
          "2) Система ДУ", "3) ДУ 2ого порядка","4) Выход из программы"]

changelist=["Решение ДУ", "1) Метод Эйлера",
            "2) Метод Рунге-Кутта", "3) Возврат в главное меню"]

while True:
    printmain()
    switch=int(input())
    if switch==1:
        while True:
            printchangelist()
            switch1=int(input())
            if switch1==1:
                metods.eler(0, 1, 10, 0, 1)
            elif switch1==2:
                metods.ruku(0, 1, 10, 0, 1)
            elif switch1==3:
                break    
    elif switch==2:
        metods.sistema(1, 1.5, 0.1, 2, 1, 1)
    elif switch==3:
        metods.vtor(1, 1.5, 0.1, 0.77, -0.44)  
    elif switch==4:
        break
    
    
print("Программа завершена")

