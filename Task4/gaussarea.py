#!/usr/bin/env python
# coding: utf-8

# In[3]:


from scipy import integrate
from math import *
import numpy as np
import matplotlib.pyplot as plt

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0
A = float(input("Give your value for A:"))
x0 = float(input("Give your value for x0:"))
sig = float(input("Give your value for sig:"))
z0 = float(input("Give your value for z0:"))
x=np.linspace(-10,10,200)
y=gauss(x, A, x0, sig, z0)

plt.plot(x,y, color="purple")
plt.title("Gaussian Function")

a=float(input("Give your value for the lower bound:"))
b=float(input("Give your value for the upper bound:"))
area, error =integrate.quad(gauss,a,b, args=(A, x0, sig, z0))
print(f"The Area between x={a} and x={b} is {area} with error {error}")

x_fill=np.linspace(a,b,100)
y_fill=gauss(x_fill,A,x0,sig,z0)
plt.fill_between(x_fill,y_fill,alpha=0.7, color="pink", label=f"Area x:[{a},{b}] ={area}")
plt.legend()
plt.show()

