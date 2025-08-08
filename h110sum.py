x,n,k=map(int,input().split())
'''
sum = 0
for i in range(1, n+1):
    sum = sum + x*(k+i)
print(sum)
'''
s = x * (n*k + n*(n+1)//2)
print(s)
