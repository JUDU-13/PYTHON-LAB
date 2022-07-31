stock = { 'Python': 45, 'C programming':20 }
print("Default list:",stock)
stock.update (Python = 35) # updating dict
print('Updated list:', stock)
popped = stock. popitem() # popping an item
print("Deleted item:", popped)
print("New List:", stock)
stock.update({'Java':55}) # Adding new item to dict
print("Final List:", stock)