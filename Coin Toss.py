import random as rn
def toss(lim):
    events=[]
    num_heads=0
    for i in range(lim):
        value=rn.randint(0,1)#0-Tails,1-Heads
        if value==1:
            num_heads+=1
            events.append("Heads")
        else:
            events.append("Tails")
    probability=num_heads/lim
    print("Occured events : ",events)
    return probability,num_heads

limit=int(input("Enter the number of times to toss the coin : "))
prob,heads=toss(limit)
print("Heads has occured {} times\nProbability of occuring heads ={}".format(heads,prob))