#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# leap year or not


def is_leap(year):
    
    
    # Write your logic here
    if year%4==0  and year%100!=0:
        leap = True
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))

