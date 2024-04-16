import string
import random

length=int(input('enter the length of password='))
arr=["1.normal","2.medium","3.complex"]
lis=""
print("Select your complexity of your password:")
for i in arr:
    print(i)
sel=int(input('enter your complexity level number'))
if sel==1:
    lis+=string.ascii_letters
elif sel==2:
    lis+=string.ascii_letters
    lis+=string.digits
elif sel==3:
    lis+=string.ascii_letters
    lis+=string.digits
    lis+=string.punctuation
else:
    print('enter a valid option')

password=[]

for i in range(length):
    rndm=random.choice(lis)
    password.append(rndm)

print("Your password is :- "+"".join(password))
