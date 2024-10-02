import math as m
def square():
    print('''\nTo get parameter of a square out of following, enter corresponding values:
    1.Area
    2.Perimeter
    3,Side
    4,Diagonal
    0.To go back to previous menu''')
    value=input()
    if value in ['1','Area','area','AREA']:
        try:
            side=float(input('Enter the length of side of the square:'))
            print(f'Area of square with side {side} is {pow(side,2)}')
            square()
        except:
            square()
    elif value=='2':
        try:
            side=float(input('Enter the length of side of the square:'))
            print(f'Perimeter of square with side {side} is {4*side}')
            square()
        except:
            square()
    elif value=='3':
        print('Do you have perimeter or area?(Enter what you have)')
        parameter=input()
        if parameter in ['AREA','Area','area','a']:
            area=input('Enter the area of the square')
            try:
                area=float(area)
                print(f'The side of square with area {area} is {pow(area,0.5)}')
                square()
            except:
                square()
        elif parameter in ['PERIMETER','Perimeter','perimeter']:
            peri=input('Enter the perimeter of the square')
            try:
                peri=float(peri)
                print(f'The side of square with perimeter {perimeter} is {peri/4}')
                square()
            except:
                square()
        else:
            square()
    elif value=='4':
        print('Do you have perimeter or area?(Enter what you have)')
        parameter=input()
        if parameter in ['AREA','Area','area','a']:
            area=input('Enter the area of the square')
            try:
                area=float(area)
                print(f'The diagonal of square with area {area} is {2**0.5*pow(area,0.5)}')
                square()
            except:
                square()
        elif parameter in ['PERIMETER','Perimeter','perimeter']:
            try:
                peri=float(input('Enter the perimeter of the square:'))
                print(f'The diagonal of square with perimeter {peri} is {2**0.5*(peri/4)}')
                square()
            except:
                square()
        else:
            square()
    elif value=='0':
        import sys
        import os
        twod_dir=r'C:/Users/hp/Appdata/Local/Programs/python/Python311/Maths/Geometry/two_d_Shapes'
        sys.path.append(twod_dir)
        import two_d as t
        t.two_d()
    else:
        print('Enter What`s available in the list')
        square()
square()
