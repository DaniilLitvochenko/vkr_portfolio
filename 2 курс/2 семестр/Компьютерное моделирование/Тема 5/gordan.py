def gordan(n, m):         
   for i in range(n):
       for k in range(n):
           if (k != i):
               q = m[k][i] / m[i][i]
               for j in range(i,n+1):
                   if (j == i):
                       m[k][j] = 0
                   else:
                       m[k][j] = m[k][j] - q * m[i][j]
  
   ans = [0 for i in range(n)]
  
   for i in range(n):
       print(m[i])
     
   for i in range(n):
       ans[i] = round(m[i][n]/ m[i][i])
   return ans

a = [[5,7,6,5,23],[7,10,8,7,32],[6,8,10,9,33],[5,7,9,10,31]]
print(gordan(4,a))

