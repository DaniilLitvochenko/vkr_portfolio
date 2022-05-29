"""
Litovchenko Daniil

2 group 3 podgroup

Задания 1: 4, 6, 20
Задания 3: 14, 4

((C∨B)→B)∧(A∧B)→B

"""

delimiter  = "*"
space_symbol = " "
# ord() или chr()stop
header = "*  A  *" + "*  B  *" + "*  C  *"+ "*  C∨B  *"+"*(C∨B)→B*"+"* (A∧B) *"+"*((C∨B)→B)∧(A∧B)*"+"*((C∨B)→B)∧(A∧B)→B*"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)

inpstr = ["*  ",[],"  **  ",[],"  **  ",[],"  *"]
resstr1 = ["*   ",[],"   *"]
resstr2 = ["*   ",[],"   *"]
resstr3 = ["*   ",[],"   *"]
resstr4 = ["*       ",[],"       *"]
resstr5 = ["*        ",[],"        *"]

for i in range(2):
    inpstr[1]=str(i)
    for j in range(2):
        inpstr[3]=str(j)
        for ij in range(2):
            inpstr[5]=str(ij)
            
            resstr1[1]=str(j or ij)
            resstr2[1]=str(int(not(resstr2[1]) or j))
            resstr3[1]=str(i and j)
            resstr4[1]=str(int(resstr2[1] and resstr3[1]))
            resstr5[1]=str(int(not(int(resstr4[1])) or j))
            print(*inpstr +resstr1+resstr2+resstr3+resstr4+resstr5, sep="")
        
print(delimiter * table_width)



