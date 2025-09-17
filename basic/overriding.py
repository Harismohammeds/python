class Demo:
    def hello(self):
        print("this is hello function")
    def hi(self):
        print("this is hi function")
class Child(Demo):
    def hello(self):
        print("this is child class function")
x=Child()
x.hello()


