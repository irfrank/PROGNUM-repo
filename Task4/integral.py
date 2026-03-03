#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
f=input("Give the function: ")
a=float(input("Give the lower bound: "))
b=float(input("Give the upper bound: "))

x=np.random.uniform(low=a, high=b, size=1000000)
y=eval(f)

integral=(b-a)*np.mean(y)

print(integral)


# In[ ]:




