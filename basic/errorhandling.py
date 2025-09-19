try:
    x=int(input("enter a number: "))
    y=int(input("enter a number: "))
    print("sum of two numbers is: ",x/y)
#except ZeroDivisionError:
#   print("cant divide by 0")
except ValueError:
    print("cant divide a string")