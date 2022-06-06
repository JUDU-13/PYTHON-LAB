email=input("Enter the email to be validated : ")
domains=["gmail.com","yahoo.com","reddit.com","sjcetpalai.ac.in","ieee.org","hotmail.com","outlook.com","zoho.com"]
words=email.split("@")
for i in domains:
    if(i==words[1]):
        print("The email is valid")
        flag=1
        break
    else:
        flag=0
if(flag==0):
    print("The email is invalid")


