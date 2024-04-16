num1=int(input('enter the number='))
num2=int(input('enter the number='))
print("Available operations")
arr=['+','-','x','^','/']
for i in arr:
    print(i)
opr=input('enter your operation=')
if opr=='+':
    print(num1+num2)
if opr=='-':
    print(num1-num2)
if opr=='x':
    print(num1*num2)
if opr=='^':
    print("if you want num1^num2 enter 1")
    print("or if you want num2^num1 enter 2")
    power=input('enter your condition=')
    if power=='1':
        print(num1**num2)
    if power=='2':
        print(num2**num1)
if opr=='/':
    print("if you want num1/num2 enter 1")
    print("or if you want num2/num1 enter 2")
    div=input('enter your condition=')
    if div=='1':
        print(num1/num2)
    if div=='2':
        print(num2/num1)
