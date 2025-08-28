num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter the operation(+/-/*// ")
x=int(num1) 
y=int(num2)
print("-"*50)
if operation=="+":
    print("The result is : "+str(x+y))
elif operation=="-":
    print("The result is : "+str(x-y))
elif operation=="*":
    print("The result is : "+str(x*y))
elif operation=="/":
     print("The result is : "+str(x/y))
print("-"*50)


