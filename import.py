import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

x = ("the radius is {:.2f}, and the area is {:.5f}.")
print(x.format(4, 3.14*4**2))

x = ((4.1**2 - 4)/.1)
print(int(x))
print(float(x))

import math 
print(math.e)
print(math.e**3)
print(math.exp(3))

import numpy as np

x = np.exp(3)
print(x)

a = 89/34
b = 34/13 
y = "({:.3f}, {:.3f})"
print(y.format(a, b))

import matplotlib.pyplot as plt 
x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]
plt.plot(x, y)
plt.show()

import numpy as np 
import matplotlib.pyplot as plt
np.set_printoptions(precision=3, suppress=1, floatmode='fixed')
def f(x):
  y = x**2
  return y


x = np.arange(0, 5.1, 0.1)
y = f(x)
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('f(x)=x^2')
plt.grid ()
plt.show()


def f(x):
    y = (1+1/x)**x
    return y 

y = f(15)
print("{:.5f}".format(y))

def pw(x):
    if x <= 0:
        y = x**2 
    else: 
        y = x + 1
    return y

y1 = pw (-1)
y2 = pw (2)
print("f({}) = {}".format(-1,y1))
print("f({}) = {}".format(2,y2))

import numpy as np 
import matplotlib.pyplot as plt 
np.set_printoptions(precision=3, suppress=1, floatmode= "fixed")

def pw(x):
    if x <= 0:
        y = x**2
    else:
        y = x + 1
    return y 

vpw = np.vectorize(pw)
a = -2
b = 0 
n = 50
dx = (b-a)/n
x = np.arange(a, b+dx, dx)
x[n] = b
y = vpw(x)
plt.plot(x,y,"b")

a = 0 
b = 2 
n = 50 
dx = (b-a)/n
x = np.arange(a+dx, b+dx, dx)
y = vpw(x)
plt.plot(x, y, "b")
plt.grid()
plt.show()

import numpy as np 
import matplotlib.pyplot as plt 
np.set_printoptions(precision=3, suppress=1, floatmode="fixed")

def pw(x):
    if x < -1:
        y = x**2
    elif -1<=x<=1:
        y = x
    else:
        y = np.sin(x)
    return y 

vpw = np.vectorize(pw)
a = -2
b = -1
n = 50 
dx = (b - a)/n 
x = np.arange(a+dx, b+dx, dx)
y = vpw(x)
plt.plot(x, y, "b")

a = -1
b = 1
n = 50 
dx = (b-a)/n
x = np.arange(a+dx, b+dx, dx)
y = vpw(x)
plt.plot(x, y, "b")

a = 1 
b = 3
n = 50 
dx = (b-a)/n
x = np.arange(a+dx, b+dx, dx)
y = vpw(x)
plt.plot(x, y, "b")
plt.show()