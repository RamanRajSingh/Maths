import math as m
#type of polyhedron
a='Cube'
#Edge measurement
def edge(a):
    s=float(input('Enter size of the edge of {}'.format(a)))
    return s
#Area
def area(a):
    s=edge(a)
    area=6*pow(s,2)
    print('Area of {} is {} square units'.format(a,area))
#Volume
def volume(a):
    s=edge(a)
    vol=pow(s,3)
    print('Volume of {} is {} cubic units'.format(a,vol))
#Diagonal
def diagonal(a):
    s=edge(a)
    dia=m.sqrt(3)*s
    print('Length of diagonal of {} is {} units'.format(a,dia))

