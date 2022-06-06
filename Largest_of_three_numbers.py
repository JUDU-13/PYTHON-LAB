
# coding: utf-8

# In[4]:


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
 
if (x>y) and (x>z):
       l=x
elif (y>x) and (y>z):
       l=y
else:
       l=z
print("The largest number is",l)

