
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_list=[1,2,3,4,5]


# In[3]:


arr=np.array(my_list)


# In[5]:


my_list=[[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


arr=np.array(my_list)


# In[7]:


arr


# In[8]:


np.arange(0,3)


# In[10]:


np.zeros((2,3))


# In[11]:


np.ones((4,4))


# In[12]:


np.eye(4)


# In[18]:


np.linspace(0,10,5)


# In[22]:


np.random.rand(4,4)


# In[23]:


np.random.randn(4,4)


# In[24]:


np.random.randint(20,100,20)


# In[25]:


np.random.randint(10,20,10)


# In[2]:


arr=np.arange(25)


# In[4]:


arr=arr.reshape(5,5)


# In[9]:


ranrr=np.random.randint(5,10,5)


# In[34]:


ranrr

 
# In[6]:


arr.shape


# In[7]:


arr.max()


# In[8]:


arr.argmax()


# In[10]:


ranrr.argmax()


# In[11]:


ranrr.argmin()


# In[13]:


ranrr.dtype


# In[14]:


arr=np.arange(10)


# In[15]:


arr


# In[16]:


arr[:6]


# In[17]:


silce_arr=arr[:6]


# In[18]:


silce_arr


# In[19]:


silce_arr[:]=23


# In[20]:


arr


# In[21]:


arr_copy=arr.copy()


# In[22]:


arr_copy


# In[23]:


arr_copy[2:4]=13


# In[24]:


arr_copy


# In[26]:


arr_2d=np.array([[1,32,45],[22,13,34],[12,13,14],[21,22,23]])


# In[27]:


arr_2d


# In[39]:


arr_2d[:2,:1]


# In[29]:


arr_2d[3][2]


# In[31]:


arr_2d[2,2]


# In[33]:


arr_2d[:2,1:]


# In[34]:


arr_2d[1:,2:]


# In[35]:


arr_2d[:2,:1]


# In[38]:


arr_2d[:1,:2]


# In[40]:


arr[arr>5]


# In[41]:


arr


# In[42]:


arr[arr<23]


# In[43]:


arr>7


# In[44]:


arr_2d=np.arange(100).reshape(10,10)


# In[45]:


arr_2d


# In[47]:


arr_2d[arr_2d>90]


# In[48]:


import numpy as np


# In[49]:


arr=np.arange(0,11)


# In[50]:


arr


# In[51]:


arr+2


# In[52]:


arr+arr


# In[53]:


arr+arr*2


# In[54]:


arr+(arr**3-arr)


# In[55]:


arr**2-arr


# In[56]:


arr**2/arr


# In[58]:


arr%6


# In[59]:


arr+arr%5


# In[60]:


np.linspace(0,1,20)


# In[4]:


import numpy as np


# In[5]:


import pandas as pd


# In[7]:


my_data=[1,2,3,4,5]
d={'q':12,'w':23,'e':32,'f':87}
labels=['a','b','c','d','e']
arr=np.array([1,2,3,4,56,6,7])


# In[8]:


series=pd.Series(my_data)
series


# In[10]:


series=pd.Series(d)
series


# In[11]:


series=pd.Series(my_data,labels)


# In[13]:


s1=pd.Series([12,13,14,12,12],['Bharath','Sharath','Bharagav','Chandana','Sanjay'])
s2=pd.Series([13,12,45,12,45],['Bharath','Sanjay','Chandana','Arjun','Mithun'])


# In[14]:


s1+s2


# In[38]:


import numpy as np
import pandas as pd

from numpy.random import randn


# In[39]:


np.random.seed(101)


# In[74]:


d=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[41]:


d


# In[25]:


d[['W','Z']]


# In[31]:


d.drop('W',axis=1,inplace=True)


# In[32]:


d


# In[33]:


d.drop('A')


# In[43]:


d['B']=d['Y']+d['Z']


# In[44]:


d


# In[48]:


d.add(12)


# In[49]:


d


# In[51]:


d.loc[['A','C'],['Z',"B"]]


# In[57]:


d.iloc[2]


# In[59]:


d[d>1]


# In[60]:


bool_d=d>1


# In[61]:


bool_d


# In[62]:


d[bool_d]


# In[66]:


d=d/d


# In[68]:


d=d**2-d


# In[70]:


d=d+2


# In[72]:


d=d**2-d


# In[75]:


d


# In[80]:


d[d['W']>0][['Y','Z','W']]


# In[82]:


d[d['Z']<0][['W','X','Y']]


# In[84]:


d[d['X']>1][['Y','Z']]


# In[85]:


d[(d['W']>0)&(d['Y']>0)][['W','Y']]


# In[86]:


d


# In[89]:


d[(d['W']<0)&(d['X']<0)&(d['Y']<0)&(d['Z']>0)][['W','Z']]


# In[90]:


d.reset_index()


# In[91]:


newstates='KA KL TN AP TS'.split()


# In[92]:


newstates


# In[93]:


d['States']=newstates


# In[94]:


d


# In[96]:


d.set_index('States')


# In[ ]:


d.fillna()

