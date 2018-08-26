
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'First line\nSecond Line')


# In[2]:


pwd


# In[3]:


myfile=open('myfile.txt')


# In[4]:


myfile.read()


# In[5]:


myfile.read()


# In[6]:


myfile.seek(0)


# In[7]:


myfile.read()


# In[8]:


myfile.seek(0)


# In[9]:


myfile.readlines()


# In[10]:


myfile.close()


# In[11]:


with open('myfile.txt') as my_newfile:
    contents=my_newfile.read()


# In[12]:


contents


# In[13]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'First line\nSecond line\nthird line')


# In[21]:


with open('myfile.txt', mode='r') as f:
    print(f.read())


# In[16]:


with open('myfile.txt',mode='a') as f:
    f.write('\n forth line')
    


# In[24]:


with open('myfile.txt',mode='r') as f:
print(f.read())


# In[25]:


with open('my_txt_file.txt',mode='w') as f:
    f.write('Gildu khan')


# In[26]:


with open('my_txt_file.txt ',mode='r') as f:
    print(f.read())


# In[27]:


pwd


# In[29]:


python_resources=open('C:\\Users\\Bharath\\Desktop\\python resources.txt','w')
python_resources.write('Basic Practice:\nhttp://codingbat.com/python\nMore Mathematical (and Harder) Practice:\nhttps://projecteuler.net/archives\List of Practice Problems:\nhttp://www.codeabbey.com/index/task_list\nA SubReddit Devoted to Daily Practice Problems:\nhttps://www.reddit.com/r/dailyprogrammer\nA very tricky website with very few hints and touch problems (Not for beginners but still interesting)\nhttp://www.pythonchallenge.com/')


# In[30]:


mylist=[1,2,3]


# In[31]:


type(mylist)


# In[32]:


a_set={12,'bhafa','wjqjqwj'}


# In[33]:


type(a_set)


# In[34]:


my_dict={'bharath':2}


# In[35]:


type(my_dict)


# In[36]:


my_tup=(12,1,23,34)


# In[37]:


type(my_tup)


# In[42]:


myname='Sharath'

if myname=='Bharath':
    print('Welcome {}'.format(myname))
elif myname=='Bharagav':
    print('Welcome {}'.format(myname))
else:
    print('May I know your name,sorry for that')
    


# In[58]:





# In[4]:


def check_india(givenstring):
     return 'india' in givenstring.lower()


# In[5]:


check_india('India is a great country')


# In[6]:


def check_bharath(givenstatement):
     return 'bharath' in givenstatement.lower()
check_bharath('Bharath is bad boy')


# In[7]:


check_bharath('bad boy')


# In[8]:


def check_boy(givenstatement):
    return 'boy' in givenstatement.lower()
check_boy('Bad boy')


# In[9]:


check_boy('Bad BOY')

