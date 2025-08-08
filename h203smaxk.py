n,k = map(int,input().split())
a = list(map(int,input().split()))
res = -1e18
for i in range(0, n-k+1):
    tong = 0
    for j in range(i, i+k-1+1):
        tong = tong + a[j]
    if tong > res:
        res = tong
print(res)
        
