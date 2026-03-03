#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#define R,S,P
R="R"
P="P"
S="S"
#player's input
player=input(f"Give S for scissors, R for rock or P for paper: ")

#computer output
rps = np.array(['R','P','S'])
indx = np.random.randint(0, len(rps), 1)
print(f"computers choice {rps[indx]}")

#judge whether it is a tie, win or loss
if player==R and rps[indx]=='P':
    print ("you lose")
elif player==R and rps[indx]=='S':
    print ("you win")
elif player==S and rps[indx]=='P':
    print ("you win")
elif player==S and rps[indx]=='R':
    print ("you lose")
elif player==P and rps[indx]=='S':
    print ("you lose")
elif player==P and rps[indx]=='R':
    print ("you win")
else:
    print("tie")

