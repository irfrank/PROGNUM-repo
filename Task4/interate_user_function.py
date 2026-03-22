#!/usr/bin/env python
# coding: utf-8

# In[4]:


from math import *
import numpy as np
from numpy import sin, cos, exp, pi
from scipy import integrate

#calculate integral of any function given

f= input("Give a function depending on x:")

def function_user(f,x):
    try:
        return eval(f)
    except NameError:
        print("Name Error: Unknown variable")
    except SyntaxError:
        print("Syntax Error: invalid mathematical expression")
    except Exceptions:
        print("Unknown Error")

print(function_user(f,2))

#calculate integral with scipy.integrate.quad()

def function(x):
    f=x**4 + e**(sin(x)+cos(x))
    return f
try:
    a=0
    b=pi
    area, error=integrate.quad(function,a,b)        
    print(f"The Area between x={a} and x={b} is {area} with error {error}")
except NameError:
    print("Name Error: Unknown variable")
except SyntaxError:
    print("Syntax Error: invalid mathematical expression")
except Exceptions:
    print("Unknown Error")
 
 #monte carlo integration
try:
    x=np.random.uniform(a, b, size=1000000)
    y_values=function(x)
    integral=(b-a)*np.mean(y_values)
    print(f"The Monte Carlo integration result: {integral}")
except NameError:
    print("Name Error: Unknown variable")
except SyntaxError:
    print("Syntax Error: invalid mathematical expression")
except Exceptions:
    print("Unknown Error")

