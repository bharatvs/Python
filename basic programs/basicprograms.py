
# coding: utf-8

# In[2]:


def pastarpattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\n")
n=5
trianglestarpattern(n)


# In[9]:


def pyramidstarreversepattern2(n):
    k=n*2-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for s in range(0,i+1):
            print("* ",end="")
        print("\n")
         
        
        
n=5
pyramidstarreversepattern2(n)


# In[18]:


def trianglestarpattern(n):
    k=n*2-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for s in range(0,i+1):
            print("* ",end="")
        print("\r")
         
        
        
n=5
trianglestarpattern(n)


# In[21]:


def numberpat(n):
    for i in range(0,n):
        for j in range(0,i+1):
            num=j
            print(num,end=" ")
            num=num-1
        print("\n")
n=5
numberpat(n)


# In[25]:


def numberpat2(n):
    k=n*2-2
    for i in range(0,n):
        for s in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            num=j
            print(num,end=" ")
            num=num-1
        print("\n")
n=5
numberpat2(n)


# In[33]:


def trianglenopattern(n):
    k=n*2-2
    for i in range(0,n):
        for s in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            num=j+1
            print(num,end=" ")
            num=num-1
        print("\r")
         
        
        
n=5
trianglenopattern(n)


# In[37]:


def trianglestarrevpattern2(n):
    k=0
    for i in range(0,n):
        num=n
        for j in range(0,num-i):
            print("* ",end="")
        for s in range(0,k):
            print(end=" ")
        k=k+3
        print("\r")
    
n=5
trianglestarrevpattern2(n):


# In[39]:


def trianglenopattern(n):
    k=0
    for i in range(0,n):
        for s in range(0,k):
            print(end=" ")
        k=k+1
        no=n
        for j in range(0,no-i):
            num=j+1
            print(num,end=" ")
            num=num-1
        print("\n")
         
        
        
n=5
trianglenopattern(n)


# In[6]:


#Program to print all words starts with s in a given sentence 
mystring="Print the words which start with s in sentence"
for words in mystring.split():
            if words[0].lower()=='s':
                print(words)
    


# In[7]:


#Print numbers from 1 to 100 and replce 3 multiple's with C and 5 multiple's with E,if number is multiple by both print Both

for num in range(1,101):
    if num%3==0 and num%5==0:
        print('Both')
    elif num%3==0:
        print('C')
    elif num%5==0:
        print('E')
    else:
        print(num)


# In[11]:


#add 'ay' to the end of the word if it is starting with vowles ,otherwise add first letter to last and add 'ay' at the last
def pig_latin(word):
    first_letter=word[0]
    if first_letter in 'aeiou':
        pig_word=word+'ay'
    else:
        pig_word=word[1:]+first_letter+'ay'
    return pig_word
pig_latin('word')


# In[27]:


#primnumber
def prime_number(n):
    num=n
    prim_no=0
    for i in range(2,n-1):
        if num%i==0:
           prim_no=+1
    
    if(prim_no==0 or n==2):
       # print(prim_no)
        print("The given Number is prime number")
    else:
        print("Tha given number is not a prime number")
            
prime_number(12)


# In[46]:


#print all prime numbers till given limit,number of prime number and sum of them
def print_prime(n):
    num=0
    sum=0
    for i in range(2,n-1):
        count=0
        for j in range(2,i-1):
            if i%j==0 or i==2:
                count=count+1
        if count==0:
            print(i)
            num=num+1
            sum=sum+i
    print(f'The total number prime numbers= {num}')
    print(f'The sum of prime numbers= {sum}')
    
print_prime(15)
        


# In[49]:





# In[50]:


shuffle(mylist)


# In[51]:


mylist


# In[1]:


int(input('Please enter a number'))


# In[ ]:


input('Please ')


# In[ ]:


input('please:'):

