
# coding: utf-8

# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[27]:


sns.set_style('whitegrid')


# In[28]:


titanic = sns.load_dataset('titanic')


# In[40]:


titanic.head()


# In[41]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[44]:


sns.distplot(titanic['fare'],bins=30,kde=False,color='red')


# In[ ]:


# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!


# In[45]:


sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')


# In[ ]:


# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!


# In[46]:


sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')


# In[ ]:


# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!


# In[47]:


sns.countplot(x='sex',data=titanic)


# In[ ]:


# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!


# In[48]:


sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')


# In[ ]:


# CODE HERE
# REPLICATE EXERCISE PLOT IMAGE BELOW
# BE CAREFUL NOT TO OVERWRITE CELL BELOW
# THAT WOULD REMOVE THE EXERCISE PLOT IMAGE!


# In[49]:


g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')

