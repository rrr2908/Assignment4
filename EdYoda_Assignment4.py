#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
res = lambda a : a + 25
print(res(10))


# In[3]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map. 
nums = []
n = int(input("Enter number of elements in list:"))
for i in range(0, n):
    ele=int(input())
    nums.append(ele)
print("Original list: ", nums)
result = map(lambda x: x + x + x, nums) 
print("\nTriple of said list numbers:")
print(list(result))


# In[4]:


# Write a Python program to square the elements of a list using map() function.
nums = []
n = int(input("Enter number of elements in list:"))
for i in range(0, n):
    ele=int(input())
    nums.append(ele)
print("Original list: ", nums)
result = map(lambda x: x*x, nums)
print(list(result))


# In[ ]:




