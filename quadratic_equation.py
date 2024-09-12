def roots(a,b,c):
    discremenant=b**2-4*a*c
    m=(-b/2*a)
    mj=((discremenant)**.5)/2*a
    n=(-b/2*a)
    nj=(-1*(discremenant)**.5)/2*a
    r1=m+mj
    r2=n+nj
    return r1,r2
    
def roots_of(a=1,b=2,c=1):
    if a==0:
        r=-c/b
        print("There is only one root which is",r)
    else:
        discremenant=b**2-4*a*c
        if discremenant<0:
            print("roots are imaginary")
            print('Roots of given equation are',roots(a,b,c))
        elif discremenant==0:
            print("roots are real and equal")
            print('Roots of given equation are',roots(a,b,c))
        else:
            print("roots are real and distinct")
            print('Roots of given equation are',roots(a,b,c))
            
