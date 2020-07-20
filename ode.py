import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return y
def df(a):
    return 1
x0=float(input("x0:"))
y0=float(input("y0:"))
step=float(input("step:"))
n=int(input("n:"))
x=[x0+step*i for i in range(n+1)]
X=np.asarray(x)
Y=np.exp(x)
y=[]
y.append(y0)
for i in range(n):
    y.append(y[i]+f(x[i],y[i])*step)
plt.plot(x,y)
plt.plot(X,Y)
plt.show()