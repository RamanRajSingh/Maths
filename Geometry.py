print('''If you want to perform following operations then enter their corresponding value:
1. Two dimensional problem(related to 2d shapes)
2. Three dimensional problem(related to 3d shapes)
3. To go back to main list''')
n=input()
if n in ['1','2d','2D']:
    import sys
    import os

    # Get the absolute path of the directory containing two_d.py
    twod_dir = r'C:\Users\hp\AppData\Local\Programs\python\Python311\Maths\Geometry\2D-Shapes'

    # Add the path to sys.path
    sys.path.append(twod_dir)

    # Now you can import two_d
    import two_d
elif n in ['2','3d','3D']:
    import sys
    import os

    # Get the absolute path of the directory containing three_d.py
    threed_dir = r'C:\Users\hp\AppData\Local\Programs\python\Python311\Maths\Geometry\3D-Shapes'

    # Add the path to sys.path
    sys.path.append(threed_dir)

    # Now you can import three_d.py
    import three_d
#Routes the user to Maths.py 
elif n == '3':
    import sys
    import os

    # Get the absolute path of the directory containing Maths.py
    math_dir = r'C:\Users\hp\AppData\Local\Programs\python\Python311\Maths'

    # Add the path to sys.path
    sys.path.append(math_dir)

    # Now you can import Maths
    import Maths
