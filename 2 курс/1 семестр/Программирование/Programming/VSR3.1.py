import random
print("**************")
print("*Угадай число*")
print("**************")
ug = random.randint(0, 100)
print("Число загадано")

a=int(input("Ваша версия? "))
while a != ug:
    if a > ug:
        print("Число {} {} загаданного".format(a, "меньше"))
        a = int(input("Попробуйте еще раз: "))
    else:
        print("Число {} {} загаданного".format(a, "больше"))
        a = int(input("Попробуйте еще раз: "))
        
print("Поздравляю, вы угадали")
