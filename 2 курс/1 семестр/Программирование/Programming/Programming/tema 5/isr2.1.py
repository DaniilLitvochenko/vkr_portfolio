def printtable(*args):
    delimiter  = "*"
    space_symbol = " "
    a=len(args)
    header=""
    for i in range (a):
        header+= "*"+"{}".format(args[i]).center(5, ' ')+"*"
    table_width = len(header)
    print(delimiter * table_width)
    print(header)
    print(delimiter * table_width)
    arggen()
    print(delimiter * table_width)

def arggen():
    for i in range(2):
        a=str(i)
        for j in range(2):
            b=str(j)
            for ij in range(2):
                c=str(ij)
                res1=i and j
                res2=i or j
                res3=i and ij
                body(a,b,c,res1,res2,res3)

def body(*args):
    text=""
    a=len(args)
    for i in range(a):
        text+="*"+"{}".format(args[i]).center(5, ' ')+"*"
    print(text)
    
printtable("A", "B", "C", "A&B", "A|B", "A&C")

