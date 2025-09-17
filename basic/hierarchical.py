class Demo:
    name="Haris"
    def hello(self):
        print("hello world")
    def hi(self):
        print("welcome to my class")
class Child(Demo):
    def home(self):
        print("this is home")
class Child2(Demo):
    def house(self):
        print("this is house")
x=Child2()
x.house