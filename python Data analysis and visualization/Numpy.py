
# coding: utf-8

# In[ ]:


#### Import NumPy as np


# In[1]:


import numpy as np


# In[ ]:


#### Create an array of 10 zeros 


# In[2]:


np.zeros(10)


# In[ ]:


#### Create an array of 10 ones


# In[3]:


np.ones(10)


# In[ ]:


#### Create an array of 10 fives


# In[4]:


np.ones(10) * 5


# In[ ]:


#### Create an array of the integers from 10 to 50


# In[5]:


np.arange(10,51)


# In[ ]:


#### Create an array of all the even integers from 10 to 50


# In[6]:


np.arange(10,51,2)


# In[ ]:


#### Create a 3x3 matrix with values ranging from 0 to 8


# In[7]:


np.arange(9).reshape(3,3)


# In[ ]:


#### Create a 3x3 identity matrix


# In[8]:


np.eye(3)


# In[ ]:


#### Use NumPy to generate a random number between 0 and 1


# In[15]:


np.random.rand(1)


# In[ ]:


#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution


# In[33]:


np.random.randn(25)


# In[35]:


np.arange(1,101).reshape(10,10) / 100


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[36]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[38]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[40]:


mat[2:,1:]


# In[41]:


mat[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[42]:


mat[:3,1:2]


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[46]:


mat[4,:]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[49]:


mat[3:5,:]


# #### Get the sum of all the values in mat

# In[50]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[51]:


mat.std()


# #### Get the sum of all the columns in mat

# In[53]:


mat.sum(axis=0)

