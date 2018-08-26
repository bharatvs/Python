
# coding: utf-8

# In[1]:


my_details=[1234,'Bharath','V','bharathkmr532']


# In[2]:


my_details[0]


# In[3]:


my_details[0:]


# In[4]:


my_details[2:]


# In[5]:


num_list=[0,1212,12,34,56,67]


# In[6]:


num_list.append(12398)


# In[7]:


num_list


# In[8]:


num_list('Bharath')


# In[9]:


num_list.append('bharath')


# In[10]:


num_list


# In[11]:


num_list.pop()


# In[12]:


num_list


# In[13]:


num_list.sort()


# In[14]:


num_list


# In[15]:


num_list.reverse()


# In[16]:


num_list


# In[17]:


my_list=[1,2,3,4,['Bharath','Sharath','Bhargav','Sanjay']]


# In[21]:


print('{} is ID of {}'.format(my_list[0],my_list[4][0]))


# In[22]:


my_dictonaries={'12':['Bharath','kmr532'],'13':['Bharagav','kb555']}


# In[26]:


my_dictonaries['12'][1].upper()


# In[28]:


my_dictonaries={'14':{'bh':1234}}


# In[29]:


my_dictonaries


# In[31]:


my_dictonaries['14']={'nh':78798}


# In[32]:


my_dictonaries


# In[33]:


my_dictonaries['15']={'boss':69}


# In[34]:


my_dictonaries


# In[35]:


my_dictonaries.values()


# In[36]:


my_dictonaries.keys()


# In[37]:


my_dictonaries.items()


# In[38]:


mytuple=(1,232,232,2323,'bharath')


# In[39]:


mytuple.count(1)


# In[40]:


mytuple.count(2)


# In[41]:


mytuple.count(232)


# In[42]:


mytuple.index(232)


# In[43]:


mytuple[1:]


# In[44]:


mytuple=mytuple[2:]


# In[45]:



mytuple


# In[46]:


mytuple[0]='2121'

