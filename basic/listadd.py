list1=[12,28,7,25,32,29,54]
def add():
    sum=0
    for i in list1:
        print(i)
        sum=sum+i
    return sum
add_sum=add()
print("Sum is :",add_sum)