import numpy as np
#O(nlogn) method
def eval(P,x):
    if len(P)==1:
        return P[0]
    else:
        A=np.zeros(len(P)//2)
        B=np.zeros(len(P)//2)
        for i in range(len(P)//2):
            A[i]=P[2*i]
            B[i]=P[2*i+1]
        k=eval(A,x**2) + x*eval(B,x**2)
        #print(k)
        return k

#O(n^2) method
def eval2(P,x):
    res=0
    for i in range(len(P)):
        res+=P[i]*(x**i)
    return res

print("O(n^2)   :",eval2([1,2,3,4,5,6,7,8],2))
print("O(nlogn) :",eval([1,2,3,4,5,6,7,8],2))