#!/usr/bin/env python
# coding: utf-8

# In[13]:


Y = float(input("year:"))
M = float(input("month:"))
D = float(input("day:"))
JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print (f"{JD}")


# In[16]:


Y1 = float(input("year of first date:"))
M1 = float(input("month of first date:"))
D1 = float(input("day of first date:"))
JD1 = 367*Y1 -7*(Y1+(M1+9)//12)//4 - 3*((Y1+(M1-9)//7)//100 + 1)//4 + (275*M1)//9 + D1 + 1721029-0.5


Y2 = float(input("year of second date:"))
M2 = float(input("month of second date:"))
D2 = float(input("day of second date:"))
JD2 = 367*Y2 -7*(Y2+(M2+9)//12)//4 - 3*((Y2+(M2-9)//7)//100 + 1)//4 + (275*M2)//9 + D2 + 1721029-0.5
print (f"{abs(JD1-JD2)}")


# 
