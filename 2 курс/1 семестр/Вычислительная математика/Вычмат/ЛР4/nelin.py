import metods

def printmain():
    for i in range(5):
        print(mainlist[i])
    print()

   
mainlist=["Главное меню", "1) Метод Ньютона",
          "2) Метод хорд", "3) Метод дихотомии","4) Выход из программы"]

while True:
    printmain()
    switch=int(input())
    if switch==1:
        metods.newton()
        print("\n")
    elif switch==2:
        metods.chord()
        print("\n")
    elif switch==3:
        metods.dichotomy()
        print("\n")
    elif switch==4:
        break
    
    
print("Программа завершена")

