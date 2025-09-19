class student:
    def __init__(self):
        self.name=input("Enter a name: ")
        self.maths=int(input("Enter the mark of maths: "))
        self.english=int(input("Enter the mark of english: "))
        self.physics=int(input("Enter the mark of physics: "))
        self.chemistry=int(input("Enter the mark of chemistry: "))
        self.biology=int(input("Enter the mark of biology: "))
    def sum(self):
        total=self.maths + self.english + self.physics + self.chemistry + self.biology
        print("Total mark :",total)
    def average(self):
        avg=self.maths + self.english + self.physics + self.chemistry + self.biology
        avg=avg/5
        print("Average mark is: ",avg)
        return avg
    def display(self):
        print("student name is: ",self.name)

from import2 import*