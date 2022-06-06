list = []
n = int(input("enter the number of elements in list: "))
print("Enter list")
for i in range(0,n):
    list.append(int(input()))
print(list)
item = int(input("enter the number to remove  "))
c = list.count(item)
for i in range(c):
    list.remove(item)
print("the list after removal: ",list)    
