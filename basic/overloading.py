class Demo:
    def hello(self,*args):
        ans=0
        for i in args:
            ans+=i
        return ans
x=Demo()
print(x.hello(5,6,7,8,9,10))