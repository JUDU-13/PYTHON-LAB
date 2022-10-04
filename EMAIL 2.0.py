valid=True
import string as st
low=st.ascii_lowercase
whole=st.ascii_letters+"_.-"+"1234567890"

email=input("Enter an email")
parts=email.split("@")
userid=parts[0]
domain=parts[1]

for i in userid:
    if i not in whole:
        valid=False
        break
dom=domain.split(".")
for i in dom[0]:
    if i not in low:
        valid=False
        break
if len(dom[1])>2:
    for i in dom[1]:
        if i not in low:
            valid=False
            break
else:
    valid=False
if valid:
    print("The entered mail id is valid")
else:
    print("The entered mail id is not valid")