#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    def __init__(self, N, M):
        self.M = M
        self.N = N
    def fibo(self):
        fibonacci=[]
        a=0
        b=1
        c=0
        while len(fibonacci)<self.N:
            fibonacci.append(a)
            c=a+b
            a=b
            b=c
        return fibonacci

    def divide(self):
        filtered=[]
        for i in self.fibo():
            if i %self.M==0:
                filtered.append(i)
                
        return filtered
    
example=Fibonacci(100,7)
print(example.fibo())
print(example.divide())

