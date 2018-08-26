
# coding: utf-8

# In[1]:


bharath=[num**5 for num in range(0,10)]


# In[2]:


bharath


# In[6]:


b=['a','b','c','d']
c=['w',2,3]


# In[11]:


bharath=[b.append(c) for c in c ]


# In[12]:


b


# In[18]:


list(map(lambda num:num*20,[1,2,34,5]))
my_list=[200,2,455,231,121]


# In[19]:


list(map(lambda num:num-24,my_list))


# In[24]:


list(filter(lambda num:num%2==0,my_list))

