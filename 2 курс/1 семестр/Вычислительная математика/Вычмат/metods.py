from math import *

def f(x):
    return (sqrt(1.7*x*x+0.5))/(1.4+sqrt(1.2*x+1.3))

def fpr1(x):
    return (1.02*x*x+(2.38*sqrt(1.2*x+1.3+2.21)*x-0.3))/(sqrt(1.2*x+1.3)*sqrt(1.7*x*x+0.5)*(sqrt(1.2*x+1.3)+1.4)**2)

def fpr2(x):
    return (1.428*x)/sqrt(1.2*x + 3.51) + 2.04*x + 2.38*sqrt(1.2*x + 3.51) #((1.428*x)/sqrt(1.2*x + 3.51) + 2.04*x + 2.38*sqrt(1.2*x + 3.51))/(sqrt(1.2*x + 1.3)*sqrt(1.7*x*x + 0.5)*(sqrt(1.2*x + 1.3) + 1.4)**2) - (0.6*(1.02*x*x + 2.38*sqrt(1.2*x + 3.51)*x - 0.3))/((1.2*x + 1.3)**(3/2)*sqrt(1.7*x*x + 0.5)*(sqrt(1.2*x + 1.3) + 1.4)**2) - (1.7*x (1.02*x*x + 2.38*sqrt(1.2*x + 3.51)*x - 0.3))/(sqrt(1.2*x + 1.3)*(1.7*x*x + 0.5)**(3/2)*(sqrt(1.2*x + 1.3) + 1.4)**2) - (1.2*(1.02*x*x + 2.38*sqrt(1.2*x + 3.51)*x - 0.3))/((1.2*x + 1.3)*sqrt(1.7*x*x + 0.5)*(sqrt(1.2*x + 1.3) + 1.4)**3)

def fpr3(x):
    return (0.714*x + 4.1769)/((x + 2.925)*sqrt(1.2*x + 3.51))

def fpr4(x):
    return 1

def trap(listarg):
    a=listarg[0]
    b=listarg[1]
    n=listarg[2]
    h=float(b-a)/n
    res=0.5*(f(a)+f(b))
    for i in range(1,n):
        res+=f(a+i*h)
    res*=h

    i=a
    m=0
    while i<=b:
        if m < abs(fpr2(i)):
            m=abs(fpr2(i))
        i+=0.01
    r=(((b-a)**3)/(12*n**2))*m
    print("Остаточный член |R|: ", abs(r))

    return res

def pryaml(listarg):
    a=listarg[0]
    b=listarg[1]
    n=listarg[2]
    h=float(b-a)/n
    i=a
    res=0
    while i<=b-h:
        res+=h*f(i)
        i+=h

    i=a
    m=0
    while i<=b:
        if m < abs(fpr1(i)):
            m=abs(fpr1(i))
        i+=0.01
    r=(((b-a)**2)/(2*n))*m
    print("Остаточный член |R|: ", abs(r))

    return res

def pryamr(listarg):
    a=listarg[0]
    b=listarg[1]
    n=listarg[2]
    h=float(b-a)/n
    i=a+h
    res=0
    while i<=b:
        res+=h*f(i)
        i+=h

    i=a
    m=0
    while i<=b:
        if m < abs(fpr1(i)):
            m=abs(fpr1(i))
        i+=0.01
    r=(((b-a)**2)/(2*n))*m
    print("Остаточный член |R|: ", abs(r))
    return res

def par(listarg):
    a=listarg[0]
    b=listarg[1]
    n=listarg[2]
    h=float(b-a)/n
    i=a+h
    nch=0
    ch=0
    while i<=b-h:
        nch+=f(i)
        i+=2*h
    i=a+2*h
    while i<=b-2*h:
        ch+=f(i)
        i+=2*h
    res=h/3*(f(a)+f(b)+4*nch+2*ch)

    i=a
    m=0
    while i<=b:
        if m < abs(fpr4(i)):
            m=abs(fpr4(i))
        i+=0.01
    r=(((b-a)**5)/(180*2*n**2))*m
    print("Остаточный член |R|: ", abs(r))

    return res

def spectrap(listarg, step):
    a=listarg[0]
    b=listarg[1]
    h=step
    i=a+h
    res=0
    while i<=b-h:
        res+=f(i)
        i+=h
    res+=(f(a)+f(b))/2
    res*=h
    return res

def met1(listarg):
    e=listarg[2]
    step=e**1/2
    res1=spectrap(listarg, step)
    res2=spectrap(listarg, step/2)
    while(abs(res2-res1)>e):
        step=step/2
        res1=spectrap(listarg, step)
        res2=spectrap(listarg, step/2)
    return res2

def specpryamr(listarg):
    a=listarg[0]
    b=listarg[1]
    n=listarg[2]
    h=float(b-a)/n
    i=a+h
    res=0
    while i<=b:
        res+=h*f(i)
        i+=h
    return res

def met2(listarg):
    a=listarg[0]
    b=listarg[1]
    hv=listarg[2]
    hs=hv/2
    n=(b-a)/hv
    res1=specpryamr((a, b, n))
    res2=0
    while abs(res2-res1)>hv:
        res1=specpryamr((a, b, n))
        a+=hs
        hd=hv/2
        res2=specpryamr((a, b, n))
        hv/=2
        hs/=2
    return res2

def double_integral(listarg):
    doublef = lambda x, y: 4*x**2+5*y
    a=listarg[0]
    b=listarg[1]
    c=listarg[2]
    d=listarg[3]
    nx=listarg[4]
    ny=listarg[5]
    hx=(b-a)/float(nx)
    hy=(d-c)/float(ny)
    res = 0
    for i in range(nx):
	    for j in range(ny):
		    xi = a + hx/2 + i*hx
		    yj = c + hy/2 + j*hy
		    res += hx*hy*doublef(xi,yj)
    return res

