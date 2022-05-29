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

def gaus(a, n):
    for k in range(0,n-1):
        for i in range(k+1, n):
            m = a[i][k]/a[k][k]
            for j in range(k,n+1):
                a[i][0] = 0
                a[i][j] = a[i][j]- m * a[k][j]
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
    print(gaus(a, n))
    
main()

