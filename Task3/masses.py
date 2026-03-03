#!/usr/bin/env python
# coding: utf-8

# In[8]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]
masses1=[]

for i in masses:
    if i > 7.349e+22:
        masses1.append (i)

print (f"new list {masses1}")


indices =slice(6,11,1)
m_slice = masses[indices]
print(f"m_slice = {m_slice}")

Sum=sum(m_slice)
N=len(m_slice)

print (f"the average is {Sum/N}")


# In[ ]:




