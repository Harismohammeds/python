num = 987654321
ans = 0
while num>0:
    n=num%10
    num=num//10
    ans=ans*10+n
print(ans)