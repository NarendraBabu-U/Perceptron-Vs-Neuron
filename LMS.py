
# coding: utf-8

# In[4]:

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# -- NORMALIZED POINTS--
y = np.array([[1,1,3],[1,1,2],[1,3,2],[1,5,2],[1,3,1],[1,2,8],[1,4,7],[1,6,7],[1,9,6],[1,8,7]])
b = np.array([1,1,1,1,1,-1,-1,-1,-1,-1])
nsamp = y.shape[0]

# -- LMS: mean square error function --
a = np.array([-1,0,1])  #initial weights
a1 = np.array([50,50,50])
eta = 0.001
while(1):
    a1 = a
    for i in range(nsamp):
        a = a + eta * (b[i]-np.dot(a,y[i])) * y[i]
    if np.sum(np.square((np.absolute(a1-a))))<=0.01:
        break


xgrid, ygrid = np.meshgrid(np.arange(0,11, 0.01), np.arange(0,11, 0.01))
xy_grid = np.c_[xgrid.ravel(), ygrid.ravel()]
cls = []
for i in xy_grid:
    cls.append(np.sign(np.dot(i,[a[1],a[2]])+a[0]))

cls = np.asarray(cls)
cls = cls.reshape(xgrid.shape)

# -- DISPLAYING THE PLOTS --
colors  =  ListedColormap(['#FF7C46', '#48C7FF'])
plt.pcolormesh(xgrid, ygrid, cls, cmap=colors)
plt.scatter([1,1,3,5,3],[3,2,2,2,1],marker='o',label='Class w1')
plt.scatter([2,4,6,9,8],[8,7,7,6,7],marker='x',label='Class w2')
plt.axis('tight')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()




# In[ ]:



