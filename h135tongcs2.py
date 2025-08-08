n,a, b = map(int, input().split())
dem = 0
for i in range(a, b + 1):
    tong = 0
    x = i
    while x > 0:
        tong += x % 10
        x = x // 10
    if tong % n == 0:
        dem += 1
print(dem)
