def headerprint():
    delimiter  = "*"
    space_symbol = " "
    header = "* A *" + "* B *" + "* "+" AvB "+"** ¬Av¬B *" +"* (A∨B)∧(¬A∨¬B) *"
    table_width = len(header)
    print(delimiter * table_width)
    print(header)
    print(delimiter * table_width)
    
def startnum():
    inpstr = ([],[])
    for i in range(2):
        inpstr[0]=str(i)
        for j in range(2):
            inpstr[1]=str(j)
    return inpstr

def res1(a, b):
    resstr = ["*   ",[],"  *"]
    resstr[1] = int(a or b)
    return resstr

"""
resstr1 = ["*   ",[],"  *"]
resstr2 = ["*   ",[],"  *"]
resstr3 = ["*        ",[],"       *"]

        resstr1[1]=int(i or j)
        resstr2[1]=int(not i or not j)
        resstr3[1]=int(resstr1[1] and resstr2[1])
        print(*inpstr+resstr1+resstr2+resstr3, sep="")
print(delimiter * table_width)
"""

def main():
    headerprint()
    print(*startnum(),sep="")

main()   




