
# coding: utf-8

# In[ ]:


s=input("Enter a string : ")
c=input("Enter the word to be replaced : ")
r=input("Enter the word to be replaced with : ")
l=s.split()


# In[16]:


for i in range(len(l)):
    if c==l[i]:
        l[i]=r
        
print("\nThe updated string is : ")
for i in range(len(l)):
        print(l[i],end=" ")

