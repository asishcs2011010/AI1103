# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mfh1Edav-qv74FRLzRi1wR_8YJ8Z3cw3
"""

# -*- coding: utf-8 -*-
"""Untitled7.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1JruPU6A2-AXb7UaWbhAsa_6eHOarsB5h
"""

# program to plot CDF
import math
import numpy as np 
import matplotlib.pyplot as plot

#defining the function for the CDF
def F_Y(y):
  if(y<0):
    return 0
  elif(y>=0) and (y<1):
    return 2*(math.sqrt(y))/3
  elif(y>=1) and (y<4):
    return (math.sqrt(y)+1)/3
  elif(y>=4):
    return 1;
  else:
    return 0  

    #plotting Cdf 
X = np.linspace(-1,6,10000000)

Y = [F_Y(y) for y in X]
plot.xlabel('y')
plot.ylabel('$F_Y(y)$')
plot.plot(X,Y)

plot.grid()
plot.show()