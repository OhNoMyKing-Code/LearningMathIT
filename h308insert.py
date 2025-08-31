n,m = map(int,input().split())
a = []
for i in range(n):
    t = list(map(int,input().split()))
    a.append(t)

tong = 0
for i in range(n):
    for j in range(m):
        tong += a[i][j]
print(tong)



