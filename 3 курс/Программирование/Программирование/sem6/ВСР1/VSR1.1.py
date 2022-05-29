#Разработка скрипта, вычисляющего произведение матриц 
# произвольной размерность с использованием Cython. 
# Замер времени вычисления. Создание отчета по 
# результатам анализа производительности.

import random
import time
import numpy as np

def main():
    a_size_n = int(input('Введите размер n матрицы A '))
    a_size_m = int(input('Введите размер m матрицы A '))
    b_size_n = int(input('Введите размер n матрицы B '))
    b_size_m = int(input('Введите размер m матрицы B '))
    if(a_size_m == b_size_n):
        A = np.array([[random.randint(1, 10) for j in range(a_size_m)] for i in range(a_size_n)])
        print(A)
        B = np.array([[random.randint(1, 10) for j in range(b_size_m)] for i in range(b_size_n)])
        print(B)
        C = A.dot(B)
        print(C)
    else:
        print('Невозможно произвести умножение матриц заданного размера')
    

start_time = time.time()
main()
print("Выполнено за ",(time.time() - start_time)," секунд")
