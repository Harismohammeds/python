list1=[28,7,20,25,29,32]
def average():
    add=0
    for i in list1:
        print(i)
        add=add+i
    return add//len(list1)
avg=average()
print("Average is :",avg)