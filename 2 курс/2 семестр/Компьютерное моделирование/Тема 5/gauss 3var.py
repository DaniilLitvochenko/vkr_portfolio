import math


def printmatrix(a):
    for i in range(len(a)):
            print(a[i])

def matrixinp(n):
    print("Введите матрицу: ")
    
    a = []
    for i in range (n):
        a.append([])
        for j in range (n):
            print("Введите значение элемента a[",i,"][",j,"]:")
            a[i].append(int(input()))

    print("Введите побочную матрицу")
    b = []
    for i in range(n):
        print("Введите значение элемента b[",i,"]")
        b.append(int(input()))
        a[i].append(b[i])
    return a

def max_mat(a,n):
    max_temp=0
    max_i=0
    max_j=0
    for i in range (n):
        for j in range (n):
            if abs(a[i][j])>abs(max_temp):
                max_temp=a[i][j]
                max_i=i
                max_j=j
    return max_i, max_j

def swap(max_i, max_j, a, n):
    temp_i=[0 for i in range(n)]
    temp_j=[0 for i in range(n)]
    
    temp_i=a[n]
    a[n]=a[max_i]
    a[max_i]=temp_i
    
    temp_j=[a[i][max_j] for i in range(n)]
    for j in range (n):
        a[j][n] = a[max_i][j]
        a[j][n] = temp_j[max_i][n]
            
            

def sosob(a,n):
    temp=[0 for i in range(n)]
    for k in range (n):
        for i in range (n):
            for j in range(n):
                swap(max_mat(a,n),a,n)
      

def gaus(a, n):
    for k in range(1,n):
        for i in range(k, n):
            m = a[i][k-1]/a[k-1][k-1]
            for j in range(1,n+1):
                a[i][j] = a[i][j]-m * a[k-1][j]
    res=[0 for i in range(n)]

    for i in range(n-1,-1,-1):
        res[i] = a[i][n]/a[i][i]
        for k in range(n-1,i,-1):
            res[i] = res[i]-a[i][k]*res[k]/a[i][i]
    res=[round(res[i]) for i in range(n)]
    return res

def main():
    print("Введите размер матрицы")
    n=int(input("Кол-во строк: "))
    a=matrixinp(n)
    printmatrix(a)
    print(max_mat(a, n))
    print(gaus(a, n))
    
    
main()
