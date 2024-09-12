import math as m
import numpy as np
import random as r
stop=[100,1000,10000,pow(10,6),pow(10,7)]
from quadratic_equation import *
def cube_roots():
#taking input of coefficient values
    a=int(input('Enter coefficient of x3\n'))
    b=int(input('Enter coefficient of x2\n'))
    c=int(input('Enter coefficient of x\n'))
    d=int(input('Enter constant of equation\n'))
    if a==0:
        roots_of(b,c,d)
    else:
        reply=input('Do you have any root or factor:\n')
        if reply in ['Y','y','Yes','yes']:
            root=int(input('Enter known factor or root:\n'))
            e=b+root*a
            f=c+root*e
            p=(f'Roots of Equation:{a}x3+{b}x2+{c}x+{d} are {roots(a,e,f),root}')
        else:
            p="Roots other than {root} are not available"
        print(p)
##Work To be done to separate interger values            
##        root=[]
##        i=0
##        while len(root)<3:
##            sol=a*pow(i,3)+b*pow(i,2)+c*i+d
##            if sol==0:
##                root.append(i)
##                i=i+0.01
##            else:
##                m=-i
##                sol=a*pow(m,3)+b*pow(m,2)+c*m+d
##                i=i+0.01
##                if sol==0:
##                    root.append(m)
##            if i==r.choice(stop):
##                print(r.choice(still))
##                break
##            print(root)    
##        if len(root)==3:
##            print("Roots of Equation:0x3+{}x2+{}x+{} are {}".format(b,c,d,root))
##        else:
##            print('Roots of given equation is out of range') 
