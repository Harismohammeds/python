class operation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        print("sum of the numbers is:",self.num1+self.num2)
    def sub(self):
        print("sub of numbers is:",self.num1-self.num2)
    def mul(self,num3):
        print("mul of numbers is:",self.num1*self.num2*num3)

x=operation(5,5)      
x.sum()
x.mul(5)   