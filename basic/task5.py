text=input("Enter a string: ")
reversed=" "
for i in range(len(text)-1,-1,-1):
    reversed+=text[i]
print("Reversed:",reversed)