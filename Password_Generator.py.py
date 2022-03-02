#!/usr/bin/env python
# coding: utf-8

# In[16]:


#RANDOM PASSWORD GENERATOR

import random
import string

print("PASSWORD GENERATOR!")
  
#DEFINE DATA

length = 12 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#COMBINE DATA
all = lower + upper + num + symbols

#USE RANDOM
temp = random.sample(all,length)

#PASWORD 
password = "".join(temp)

print(password)

