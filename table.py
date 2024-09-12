import math as m
import random as r
def table(length=10):
    num=['multiplication table number','times table number','number whose table you want']
    a=int(input('Enter '+r.choice(num)+':'))
    for i in range(length+1):
        print(a,'x',i,'=',a*i)
