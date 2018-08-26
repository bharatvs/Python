
# coding: utf-8

# In[5]:


import array

def find_largest(arr,arr_size):
    largest=0
    for i in range(arr_size):
        if arr[i]>largest:
            largest=arr[i]
    print(largest)
arr=array.array('i',[32,91,3,14,5,6,222,2222999,2222,2223,23211])
find_largest(arr,len(arr))
            

