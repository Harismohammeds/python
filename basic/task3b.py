year=int(input("Enter your birth year :"))
age=2025-year
print("-"*50)
if age==18:
    print("You are still in teenage but you can vote")
    print("-"*50)
elif age>=19:
    print("You can vote")
    print("-"*50)
elif age<18:
    print("You are in teenage you cant vote")
    print("-"*50)
