import math
#type of polyhedron
a='cuboid'
#edge measurement
def edge(a):
    l=float(input('Enter the length of {}:'.format(a)))
    b=float(input('Enter the breadth of {}:'.format(a)))
    h=float(input('Enter the height of {}:'.format(a)))
    return l,b,h
#area
def area(a):
    l,b,h=edge(a)
    area=2*(l*b+l*h+b*h)
    print('Area of {} is {} square units'.format(a,area))
#Volume
def volume(a):
    l,b,h=edge(a)
    vol=l*b*h
    print('Volume of {} is {} cubic units'.format(a,vol))
#Diagonal
def diagonal(a):
    l,b,h=edge(a)
    dia=math.sqrt(pow(l,2)+pow(b,2)+pow(h,2))
    print('Length of diagonal of {} is {} units'.format(a,dia))
