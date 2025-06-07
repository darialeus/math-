
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x-x**3

x_values= np.linspace(-2, 2, 100)
y_values = f(x_values)
a = f(1)
b = (1)
c = f(-1)
d = (-1)
plt.figure(figsize=(10,8))
plt.plot(x_values, y_values, label="y=3x-x^3", color="k")

plt.xlabel("x")
plt.ylabel("y")
plt.plot(b, a, marker = 'o', color = "r")
plt.plot(d, c, marker = "o", color = "r")
plt.grid(True)
plt.title("Plot of y=3x-x^3")


def f (x):
    return (np.log(x))/x**(1/2)

x_values=np.linspace(6, 8, 100)
y_values= f(x_values)
b = (f(np.exp(2)))
a = np.exp(2)

plt.figure(figsize=(10,8))
plt.plot(x_values, y_values, label = "f(x) = ln(x)/sqr(x)")
plt.plot(a, b, marker = "o", color = "r")
plt.grid(True)
plt.title("Plot of f(x) = ln(x)/sqr(x)")


def f (x):
    return (x**4)/(1+x)**3

x_values=np.linspace(-4.1, -3.9, 100)
y_values= f(x_values)

c = f(-4)
d = (-4)
plt.figure(figsize=(10,8))
plt.plot(x_values, y_values, label = "f(x) = x^4/(1+x)^3")

plt.plot(d, c, marker ="o", color = "r")
plt.grid(True)
plt.title("Plot of f(x) = x^4/(1+x)^3")


def f(x):
    return 1 + x**2 - (x**4/2)

x_values = np.linspace (-2, 2, 100)
y_values = f(x_values)

a = f(1)
b = (1)
c = f(-1)
d = (-1)

plt.figure(figsize=(8,8))
plt.plot(x_values, y_values, label = "y = 1 + x^2 - x^4/2")
plt.grid(True)
plt.plot(b, a, marker = "o", color = "r")
plt.plot(d, c, marker ="o", color = 'r')
plt.title("Plot of f(x)= 1 + x^2 - x^4/2")

def f (x):
    y = ((1+x)/(1-x))**4
    return y 
    
x_values = np.linspace(-1.1, -0.90, 100)
y_values = f(x_values)

a = f(-1)
b = (-1)

plt.figure(figsize=(10,8))
plt.plot(x_values, y_values, label = "y = ((1+x)/(1-x))^4")
plt.grid(True)
plt.plot(b, a, marker = "o", color = "r")
plt.title("Plot of f(x)= ((1+x)/(1-x))^4")

def f (x):
    return np.exp(-2*x)*np.sin(x)**2

x_values = np.linspace(0, 2, 100)
y_values = f(x_values)

a = f(np.pi/4)
b = (np.pi/4)

plt.figure(figsize=(10,8))
plt.plot(x_values, y_values, label = "y = e^(-2x)*sin^2(x)")
plt.plot(b, a, marker = "o", color = 'r')
plt.grid(True)
plt.title("Plot of f(x)= e^(-2x)*sin^2(x)")
plt.show()