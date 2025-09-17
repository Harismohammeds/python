class Demo:
    name="Haris"
    def hello(self):
        print("hello world")
    def hi(self):
        print("welcome to my class")
class Child(Demo):
    pass
x=Child()
x.hello()