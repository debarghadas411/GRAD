import numpy as np
def F(x):
    A = np.ones(x, dtype=int)
    if x%2==0:
        #print(2)
        f(A,2)

    else:
        #print(1)
        f(A,1)



def f(A,op):
    fl=0
    lt=len(A)
    while fl<lt and A[fl]==0:
        fl+=1
    if fl==lt:
        return
    if op==1:
        if A[-1]==1:
            A[-1]=0
        else:
            A[-1]=1
        print(1,end=',')
        f(A,2)
    else:
        i=-1
        c=0
        while A[i]==0:
            c+=1
            i-=1
        if (c+2)<=lt:
            if A[i-1]==1:
                A[i-1]=0
            else:
                A[i-1]=1
            print(-i+1,end=",")
            f(A,1)
    return

F(1)
print()
F(2)
print()
F(3)
print()
F(4)
print()
F(5)
print()
F(6)
print()