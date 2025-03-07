import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
s="-y+sin(x)"
z=Symbol("x")
w=Symbol("y")
F=parse_expr(s)



#  variables to be read S-> striing of equation 
#  x0,y0 initial condition
#  xf ->  x to stop at it , n-> number of interval slices
# output is the graph drawn of the equation
 
x0 = 0
y0 = 1
xf = 10
n = 101
delta=(xf-x0)/(n-1)
x = np.linspace ( x0 , xf , n )
y = np.zeros ( [ n ] )
y [ 0 ] = y0
for i in range ( 1 , n ) :
   y [i]= delta * F.evalf(subs={z:x[i-1], w:y[i-1]})+y[i-1]
for i in range ( n ) :
   print ( x [ i ] , y [ i ] )

plt.plot(x,y,'o')
plt.xlabel (" Value of x " )
plt.ylabel (" Value of y " )
plt.title ("Approximate S ol u ti o n with Forward Euler ’ s Method " )
plt.show ( )



#----------------------------------------------------------------------
#
# heun.py
#
# calculate the curve which is the solution to an ordinary differential
# equation with an initial value using Heun's method
#


import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
s="y"
z=Symbol("x")
w=Symbol("y")
F=parse_expr(s)
#  variables to be read S-> striing of equation 
#  x0,y0 initial condition
#  h->stepsize

# we will use the differential equation y'(t) = y(t).  The analytic solution is y = e^t.

def y1(x,y):
    return F.evalf(subs={z:x, w:y })

def asol(x):
    return math.exp(x)

yasol = np.vectorize(asol)

h = 0.5
x0 = 0.0
y0 = 1.0

x = np.arange(0.0, 5.0, h)
y = np.zeros(x.size)
y[0] = y0

for i in range(1, x.size):
    y_intermediate = y[i-1] + h*y1(x[i-1],y[i-1])

    y[i] = y[i-1] + (h/2.0)*(y1(x[i-1],y[i-1]) + y1(x[i],y_intermediate))
    

plt.plot(x,y,'r-')