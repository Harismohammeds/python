from import1 import*
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