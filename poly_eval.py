import numpy as np
#O(nlogn) method
def eval(P,x):
    if len(P)==1:
        return P[0]
    else:
        A=np.zeros(len(P)//3)
        B=np.zeros(len(P)//3)
        C=np.zeros(len(P)//3)
        for i in range(len(P)//3):
            A[i]=P[3*i]
            B[i]=P[3*i+1]
            C[i]=P[3*i+2]
        k=eval(A,x**3) + x*eval(B,x**3) + x*x*eval(C,x**3)
        #print(k)
        return k

#O(n^2) method
def eval2(P,x):
    res=0
    for i in range(len(P)):
        res+=P[i]*(x**i)
    return res

print("O(n^2)   :",eval2([1,2,3,4,5,6,7,8,9],2))
print("O(nlogn) :",eval([1,2,3,4,5,6,7,8,9],2))