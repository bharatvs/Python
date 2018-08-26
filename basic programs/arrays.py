
# coding: utf-8

# In[ ]:


import array

first_largest=0
second_largest=0

arr=array.array('i',[345,7,2,3,4,8,6,11,21,13])
for i in range(0,len(arr)):
    for j in range(1,len(arr)):
        if arr[i]>arr[j]:
            first_largest=arr[i]
            arr[j]=arr[i]
        elif arr[i]>first_largest and arr[i]!=a[j]:
             second_largest=arr[i]
             arr[j]=arr[i]
            
        
          
            
print(first_largest)
print(second_largest)


# In[11]:


import array
def print1stand2nd(arr,arr_size):
    first=0
    second=0
    for i in range(arr_size):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i]!=first:
            second=arr[i]
    print(second)
    print(first)


# In[12]:


arr=array.array('i',[91,93,95,132,4,5,6,7,8,12,121])

print1stand2nd(arr,len(arr))

