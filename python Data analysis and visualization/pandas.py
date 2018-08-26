
# coding: utf-8

# In[1]:



# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[1]:


import pandas as pd
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[3]:


my_data=pd.DataFrame(data)
my_data
pd.concat([])


# In[8]:


my_data.groupby('Company').describe().transpose()['FB']


# In[5]:


my_data.groupby('Company').mean()


# In[6]:


my_data.groupby('Company').std()


# In[11]:


my_data.groupby('Company').max()


# In[15]:


my_data.groupby('Company').describe().transpose()['FB']


# In[18]:


my_data.groupby('Company').describe().transpose()['GOOGmy_data']


# In[21]:


my_data.groupby('Company').describe().transpose()['MSFT']


# In[1]:


data={'col1':[11,22,33,44,55],'col2':[121,223,121,456,123],'col3':['B&G','G&B','Khamadenu','HometoHome','Cowtohome']}
import pandas as pd
df=pd.DataFrame(data)
df


# In[5]:


len(df['col2'].unique())


# In[7]:


def square(x):
    return x**2
    


# In[9]:


df['col1'].apply(lambda x:x*2)


# In[13]:


df['col2'].value_counts()


# In[14]:


df.columns


# In[16]:


df.index


# In[17]:


df.sort_values('col2')


# In[18]:


df.sort_values(by='col3')


# In[19]:


df.isnull()


# In[21]:


import pandas as pd


# In[24]:


pwd

