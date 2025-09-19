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
class child(student):
    def grade(self):
        avg=self.average()


        if avg >90:
            print("your grade is A+")
        elif avg  >80:
            print("your grade is A")
        elif avg >70:
            print("your grade is B+")
        elif avg >60:
            print("your grade is B")
        elif avg >50:
            print("your grade is C+")
        elif avg >40:
            print("your grade is C")
        elif avg >30:
            print("your grade is D+")
x=child()
x.display()
x.average
x.grade()