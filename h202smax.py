n = int(input())
a = list(map(int,input().split()))
res = -1e18
for i in range(0, n-3+1):
    tong = a[i] + a[i+1] + a[i+2]
    if tong > res:
        res = tong
print(res)
        
