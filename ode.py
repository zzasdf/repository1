import numpy as np



def Euler(f,x0,y0,step,n):
    N=int(n)
    x=np.arange(N+1)
    x=x*step+x0
    dim=y0.shape[0]
    y=np.zeros((N+1,dim))
    y[0]=y0
    for i in range(1,N+1):
        y[i]=y[i-1]+f(x[i-1],y[i-1])*step
    return x,y
