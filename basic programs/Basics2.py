
# coding: utf-8

# In[6]:


#prints samller number when both are even otherwise prints larger number
def print_number(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            print(b)
        else:
            print(a)
    else:
        if a>b:
            print(a)
        else:
            print(b)
print_number(7,5)

