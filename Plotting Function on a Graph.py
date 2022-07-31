import  matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
ans = []
for i in x:
    y = (i**4)+5 # y=(x^4)+5
    ans.append(y)
    
print("Input values: ", x, "\nCalculated values:", ans)
plt.plot(ans)
plt.title("Normal Graph")
plt.xlabel('X : axis')
plt.ylabel('Y : axis')
plt.grid()
plt.show()