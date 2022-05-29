"""
Litovchenko Daniil

2 group 3 podgroup

Задания 1: 4, 6, 20
Задания 3: 14, 4

A∧B∨B→¬(A∧¬B↔¬A→B∧¬A)

"""

delimiter  = "*"
space_symbol = " "
# ord() или chr()stop
header = "*  A  *" + "*  B  *"+"*A∧B∨B*"+"**"+"*¬(A∧¬B↔¬A→B∧¬A)*"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)

inpstr = ["*  ",[],"  **  ",[],"  *"]
resstr1 = ["*  ",[],"  *"]
resstr2 = ["*  ",[],"  *"]

for i in range(2):
    inpstr[1]=str(i)
    for j in range(2):
        inpstr[3]=str(j)
        resstr1[1]=str(i and j or j)
        resstr2[1]=str(int(not(i and not j == i or j and not i)))
        print(*inpstr+resstr1+resstr2, sep="")
        
print(delimiter * table_width)



