
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


import numpy as np
 
x=np.linspace(0,5,11)
y=x**2


# In[17]:


plt.plot(x,y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')


# In[21]:


plt.subplot(1,4,1)
plt.plot(x,y,'r')
plt.subplot(1,4,2)
plt.plot(y,x,'b')
plt.subplot(1,4,3)
plt.plot(x,y,'b')
plt.subplot(1,4,4)
plt.plot(y,x,'r')


# In[24]:


fig=plt.figure()

axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Title')


# In[40]:


fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)
axes2=fig.add_axes([0.1,0.4,0.5,0.5])
axes2.plot(y,x)
axes1.set_xlabel('XL')
axes1.set_ylabel('YL')
axes1.set_title('LARGER')
axes2.set_xlabel('XS')
axes2.set_ylabel('YS')
axes2.set_title('SMALLER')


# In[44]:


fig,axes=plt.subplots(nrows=4,ncols=4)

plt.tight_layout()


# In[47]:


fig,axes=plt.subplots(nrows=1,ncols=2)
#axes[0].plot(x,y,'r')
#axes[1].plot(y,x,'b')
for current_axes in axes:
    current_axes.plot(x,y)


# In[52]:


fig=plt.figure(figsize=(8,5),dpi=100)


# In[64]:


fig,axes=plt.subplots(figsize=(19,1))
axes.plot(x,y)


# In[65]:


fig.savefig("filename.png")


# In[73]:


fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(x,x**2,label="x**2")
axes.plot(x,x**3,label="x**3")
axes.legend(loc=4)


# In[74]:


fig,ax=plt.subplots()
ax.plot(x,x**2,'b.-')
ax.plot(x,x**3,'r--')


# In[82]:


fig,axes=plt.subplots(nrows=1,ncols=3)
axes[0].plot(x,x**2,x,x**3)
axes[0].set_title('Default')

axes[1].plot(x,x**2,x,x**3)
axes[1].axis('tight')
axes[1].set_title('Tight')

axes[2].plot(x,x**2,x,x**3)
axes[2].set_ylim([0,60])
axes[2].set_xlim([2,5])


# In[83]:


plt.scatter(x,y)


# In[88]:


from random import sample
data=sample(range(0,100),10)
plt.hist(data)


# In[92]:


data=[np.random.normal(0,std,100) for std in range(1,4)]

plt.boxplot(data,vert=True,patch_artist=True)

