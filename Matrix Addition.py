import numpy as np
rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of First Matrix:")
m1= [[int(input()) for i in range(column)] for i in range(rows)]
print("First Matrix is: ")
for n in m1:
    print(n)
m1 = np.array(m1)

print("Enter the elements of Second Matrix:")
m2= [[int(input()) for i in range(column)] for i in range(rows)]
print("Second Matrix is: ")
for n in m1:
    print(n)
m2 = np.array(m2)

print("SUM=",m1+m2)