
# coding: utf-8

# In[10]:


def tsa(r,h):
    TSA=2*3.14*r*(r+h)
    return TSA


# In[19]:


def csa(r,h):
    CSA=2*3.14*r*h
    return CSA


# In[21]:


def v(r,h):
    V=3.14*r*h
    return V


# In[22]:


r=float(input("Enter the radius of the cylinder :"))
h=float(input("Enter the height of the cylinder :"))
print("Total Surface Area of Cylinder :",tsa(r,h))
print("Curved Surface Area of Cylinder :",csa(r,h))
print("Volume of Cylinder :",v(r,h))

