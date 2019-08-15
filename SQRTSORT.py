import math
def SQRTSORT(A,k,n):
    #print(k,n)
    rt=int(math.ceil(math.sqrt(n)))
    if rt<=2:
        if n==1:
            return
        elif n==2 and A[k]>A[k+1]:
            (A[k],A[k+1])=(A[k+1],A[k])
        elif n==3 or n==4:
            B=A[k:k+n]
            B.sort()
            for i in range(n):
                A[k+i]=B[i]
        return
    for i in range(0,n-rt+1):
        SQRTSORT(A,i,rt)
    SQRTSORT(A,0,n-rt+1)
A=[1,9,2,8,3,7,4,6,5]
SQRTSORT(A,0,9)
print(A)