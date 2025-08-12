import math
n = int(input())
a = list(map(int, input().split()))
kq = a[0]
for i in range(1, n):
    kq = math.lcm(kq, a[i])
print(kq)