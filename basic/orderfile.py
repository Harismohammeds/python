import csv
with open("Info.csv","w") as file:
    x=["Id","Name","Age","Country"]
    writer=csv.DictWriter(file,fieldnames=x)
    writer.writeheader()
    writer.writerow({"Id":1,"Name":"Alice","Age":30,"Country":"USA"})
    writer.writerow({"Id":2,"Name":"Bob","Age":40,"Country":"UK"})
    writer.writerow({"Id":3,"Name":"John","Age":20,"Country":"Canada"})
    writer.writerow({"Id":4,"Name":"Charlie","Age":29,"Country":"Australia"})