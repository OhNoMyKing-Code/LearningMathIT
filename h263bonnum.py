import math
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
resa = a[0]
for i in range(1,len(a)):
    resa = math.gcd(resa,a[i])

resb = b[0]
for i in range(1,len(b)):
    resb = math.gcd(resb,b[i])
if resa > resb:
    print(1,resa)
else:
    print(2,resb)