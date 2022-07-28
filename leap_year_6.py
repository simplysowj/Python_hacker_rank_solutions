#!/usr/bin/env python
# coding: utf-8

# Task
# 
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
# 
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
# 
# Constraints
#  year>=1900 and year<=100000
# 
# 

# In[7]:


def is_leap(year):
    
    if(year>=1900 and year<=100000):
        leap = False
        if(year %400 == 0):
            leap = True
        elif year % 100 ==0:
            leap =False
        elif year % 4 == 0:
            leap = True
        print(leap)
    else :
        print("ENter valid number between 1900 and 100,000")
       
  
    
    

year = int(input())
is_leap(year)


# In[ ]:




