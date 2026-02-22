#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = float(input("give the value for a, it can't be zero, a="))
b = float(input("give the value for b="))
c = float(input("give the value for c="))

if a==0:
    print("this does not work")
else:
    
    x1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    x2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    D=(b**2)-(4*a*c)
    if D>0:
        print(f"x1={x1} and x2={x2}")
    elif D==0:
        print(f"x={-b/(2*a)}")
    elif D<0:
        print("no solutions")


# In[ ]:




