import metods

def printmain():
    for i in range(6):
        print(mainlist[i])
    print()

   
mainlist=["Главное меню", "1) Логарифм",
          "2) Арктангенс", "3) Метод Чебышева(exp)",
          "4) Метод Чебышева (sin)", "5) Выход из программы"]

array_ln = [0, 0.9974442, -0.471289, 0.2256685, -0.0587527]
array_arctan = [0.9999999953, -0.3333329248, 0.199989259, -0.1427243942, 0.1101791217, -0.0867899197, 0.0647029924,
               -0.0411720745, 0.0197433754, -0.0060738765, 0.0008766095]
array_exp = [0.9999998, 1.000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
array_sin = [1.000000002, -0.166666589, 0.08333075, -0.000198107, 0.000002608]

while True:
    printmain()
    switch=int(input())
    if switch==1:
        metods.logarithm(array_ln)
        print("\n")
    elif switch==2:
        metods.arctan(array_arctan)
        print("\n")
    elif switch==3:
        metods.cheb_exp(array_exp)
        print("\n")
    elif switch==4:
        metods.cheb_sin(array_sin)
        print("\n")
    elif switch==5:
        break
    
    
print("Программа завершена")

