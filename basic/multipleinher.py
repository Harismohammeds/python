class main:
    def menu(self):
        print("this is main")
class Demo:
    name="Haris"
    def hello(self):
        print("hello world")
    def hi(self):
        print("welcome to my class")
class Child(Demo):
    def home(self):
        print("this is home")
class Akash(main,Demo):
    def home(self):
        print("this is house")
x=Akash
x.home()