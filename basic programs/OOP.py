
# coding: utf-8

# 67+56

# In[32]:


pow(2,5)
s='hello'
#s.isalnum()
#s.isalpha()
#s.islower()
#s.isupper()
s.isspace()

s=set()
s.add(1)
s.add(23)
s1={1,23,4,5}
print(s.difference(s1))


# In[16]:


class Car():
    vehical_type='Car'
    def __init__(self,brand,color,price,engine):
        self.brand=brand
        self.color=color
        self.price=price
        self.engine=engine
    def drive(self,acceletor_range):
        print('driving {} and {} {}'.format(self.color,self.brand,Car.vehical_type))
        
        


# In[41]:


s1={1,2,3,45,6}
s2={1,2,4,5,6}
#s.difference(s2)
s1.difference_update(s)
s1.discard(45)
s1


# In[53]:


s1={1,2,3}
s2={1,2,3,4,5,6}
s1.issubset(s2)
s2.issuperset(s1)


# In[30]:


my_car=Car('TATA','Black',1000000,'1000cc')
my_car.drive(1200)


# In[35]:


class Home():
    def __init__(self,area):
        self.area=area
    def print_area(self,price):
        print(f'Home total area is {self.area} and price is {price}')


# In[36]:


my_home=Home('30*40')


# In[37]:


my_home.print_area(10000)


# In[18]:


class Hotel():
    def __init__(self,name):
        self.name=name
    def hotel_type(self):
        raise NotImplementedError("Subclass must implement hotel_type")
    def staters(self):
        raise NotImplementedError("subclass must implement staters")
    def curries(self):
        raise NotImplementedError("subclassmust implement curries")
    def maincourse(self):
        raise NotImplementedError("subclass must implement maincourse")


# In[26]:


class AandB(Hotel):
    def __init__(self,name):
        self.name=name
    def hotel_type(self):
        print("Hi,\n This is a Non-Veg hotel")
    def staters(self):
        print("Hi,\n\t\t I belive you are Good and came enjoy here\n")
        print("Available staters are 1.Gobi\n 2.Panner munchurian")
    def curries(self):
        print("Hi,\n I belive you are Good and came enjoy here\n")
        print("Available curries are 1.dal \n 2.Panner masala")
    def maincourse(self):
        print("Hi,\n I belive you are Good and came enjoy here\n")
        print("Available maincourse are 1.Chappathi\n 2.Biryani")


# In[27]:


select_hotel=AandB('AandB')


# In[28]:


select_hotel.hotel_type()


# In[35]:


class Eggs():
    def __init__(self,name,total_eggs):
        self.name=name
        self.total_eggs=total_eggs
    def __str__(self):
        return f"This are {self.name}"
    def __len__(self):
        return self.total_eggs
    def __del__(self):
        print("Eggs sold out")
    


# In[36]:


my_eggs=Eggs('Chiken_Eggs',10000)


# In[37]:


print(my_eggs)


# In[38]:


len(my_eggs)


# In[41]:


pwd


# In[40]:





# In[16]:


my_string{:5}


# In[17]:


my_string[::4]


# In[18]:


my_string=my_string[::2]


# In[19]:


my_string


# In[20]:


'Hello World'[9]


# In[21]:


'tinker'[1:3]


# In[22]:


h='BHRATH'


# In[23]:


h.islower()


# In[24]:


h.lower()


# In[31]:


h.index(h)


# In[35]:


print(h.index(h))


# In[36]:


h.split(h)


# In[38]:


print('The {} {} {}'.format('great','Indian','lover'))


# In[43]:


print('Bhargav {3} {2} {0} {1}'.format('bad','boy','a','is'))*2


# In[42]:




