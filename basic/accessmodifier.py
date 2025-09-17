class Demo:
    _name="Haris"
    def hi(self):
        self.__hello()
        print("welcome to my class")
    def _welcome(self):
        print("welcome to my class")
    def __hello(self):
        print("hello world")
x=Demo()
x.hi()
