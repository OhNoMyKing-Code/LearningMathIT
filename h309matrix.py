n, m = map(int, input().split())
tong = 0

for i in range(n):
    dong = list(map(int, input().split()))
    for j in range(m):
        tong += dong[j]

print(tong)
