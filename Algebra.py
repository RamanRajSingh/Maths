from cubic_equation import *
from quadratic_equation import *
import random
still=['Work in progress!', 'Scientist at work', 'Your query will be replied soon!', 'Try again later']
while input!="Exit" or 'exit' or 'quit' or 'Ok' or 'ok' or 'Quit':
    print("\n")
    print('''For roots of following equations enter the corresponding integer:
1. Quadratic equation (of form ax^2+bx+c=0)
2. Cubic equation (of form ax^3+bx^2+cx+d=0)
3. Linear equation (of form ax+by+c=0''')
    choice=input()
    if choice in ['1' , 'Quadratic' , 'quadratic' , 'two variable' , 'first','I','१','१.']:
        x=['a','coefficient of x^2', 'coefficient of highest power of x']
        print('Enter the value of ',random.choice(x))
        a=int(input())
        y=['b','coefficient of x', 'coefficient of second highest power of x']
        print('Enter the value of ',random.choice(y))
        b=int(input())
        z=['c','constant', 'coefficient of least power of x','coefficient of x^0']
        print('Enter the value of ',random.choice(z))
        c=int(input())
        roots_of(a,b,c)
    elif choice in ['2' ,'cubic' ,2 ,'2.','second','II''२','२']:
        cube_roots()
    elif choice in ['3',3,'3.','linear','III']:
        print(random.choice(still))
    else:
        re=['Review your choice!','Try again!','Try something else!','This is what you want? {}'.format(choice), 'Is {} available in options?'.format(choice),'नेकी मत कर तो जूते खा!']
        print(random.choice(re))
