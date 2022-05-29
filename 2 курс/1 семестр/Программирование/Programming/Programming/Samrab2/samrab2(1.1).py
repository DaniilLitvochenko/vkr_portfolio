"""
Litovchenko Daniil

2 group 3 podgroup

Задания 1: 4, 6, 20
Задания 3: 14, 4

(A∨B)∧(¬A∨¬B)

"""

delimiter  = "*"
space_symbol = " "
# ord() или chr()stop
header = "* A *" + "* B *" + "* "+" AvB "+"** ¬Av¬B *" +"* (A∨B)∧(¬A∨¬B) *"

table_width = len(header)
# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)

inpstr = ["* ",[]," ** ",[]," *"]
resstr1 = ["*   ",[],"  *"]
resstr2 = ["*   ",[],"  *"]
resstr3 = ["*        ",[],"       *"]
for i in range(2):
    inpstr[1]=str(i)
    for j in range(2):
        inpstr[3]=str(j)
        resstr1[1]=int(i or j)
        resstr2[1]=int(not i or not j)
        resstr3[1]=int(resstr1[1] and resstr2[1])
        print(*inpstr+resstr1+resstr2+resstr3, sep="")
        
print(delimiter * table_width)



