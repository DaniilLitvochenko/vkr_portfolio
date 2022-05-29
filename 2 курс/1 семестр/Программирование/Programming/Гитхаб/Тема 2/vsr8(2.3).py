"""

Перепишите лямбда-функцию, генерирующую квадраты
чисел из переменной типа list, через генератор списка.

"""

import random

class Main:
    
    @staticmethod
    def generator(n,r):
        listarg = []
        for i in range (n):
            listarg.append(random.randint(0, r)) 
        return listarg

    @staticmethod
    def main():
        r = int(input("Введите верхнюю границу диапазона случайных чисел: "))
        n = int(input("Введите количество элементов: "))
        gen = Main.generator(n, r)
        print(gen)
        print(list(map(lambda x: x*x, gen)))   
        
        
Main.main()
