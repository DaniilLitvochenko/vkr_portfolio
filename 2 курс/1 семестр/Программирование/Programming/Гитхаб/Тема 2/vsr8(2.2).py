import random

class Main:
    @staticmethod
    def generator(n, r):
        listargs = []
        for i in range(n):
            listargs.append(random.randint(0, r))
        return listargs
    
    @staticmethod
    def similar(n, args):
        reslist = set(args)
        return list(reslist)
    
    @staticmethod
    def result():
        print("Введите кол-во элементов: ")
        n = int(input())
        print("Введите верхнюю границу диапазона случайных чисел: ")
        r = int(input())
        arg = Main.generator(n, r)
        print("Элементы: ", arg)
        print("Неповторяющиеся: ", Main.similar(n, arg))
    
Main.result()
