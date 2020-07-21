import ode
import numpy as np
import matplotlib.pyplot as plt
def qwe(x,y):
    re=np.zeros(2)
    re[0]=y[1]
    re[1]=-y[0]
    return re

X,Y=ode.Euler(qwe,0,np.array([1,0]),0.001,60000)
plt.plot(X,Y[:,0])
plt.plot(X,np.cos(X))
plt.show()
