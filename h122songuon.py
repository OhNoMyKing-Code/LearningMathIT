m = int(input())
ans = -1
for x in range(m - 100, m): 
    if x <= 0:
        continue
    tong = x
    t = x
    while t > 0:
        tong += t % 10
        t = t // 10
    if tong == m:
        ans = x
        break

print(ans)

