# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# -- NORMALIZED POINTS--
y = np.array([[1,1,3],[1,1,2],[1,3,2],[1,5,2],[1,3,1],[-1,-2,-8],[-1,-4,-7],[-1,-6,-7],[-1,-9,-6],[-1,-8,-7]])
nsamp = y.shape[0]

# -- Single sample perceptron --
a = np.array([-1,0,1])  #initial weights
c = 0
k = 0

while(c!=nsamp):
    c = 0
    for k in range(nsamp):
        if (np.dot(a,y[k])<=0):
            a = a+y[k]
        else:
            c+=1

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


