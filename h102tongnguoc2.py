a, b = map(int, input().split())
dem = 0
tong = 0
for n in range(a, b + 1):
    s = 0
    i = 1
    while i <= n:
        if n % i == 0:
            s += i
        i += 1
    if s == 2 * n:
        dem += 1
        tong += n
print(dem, tong)
