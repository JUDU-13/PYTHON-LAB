def tsa(r,h):
    TSA=2*3.14*r*(r+h)
    return TSA

def csa(r,h):
    CSA=2*3.14*r*h
    return CSA

def v(r,h):
    V=3.14*r*h
    return V

r=float(input("Enter the radius of the cylinder :"))
h=float(input("Enter the height of the cylinder :"))
print("Total Surface Area of Cylinder :",tsa(r,h))
print("Curved Surface Area of Cylinder :",csa(r,h))
print("Volume of Cylinder :",v(r,h))
