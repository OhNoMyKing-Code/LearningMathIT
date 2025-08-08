n = int(input())
dem = 0
tong = 0
while n > 0:
    chuso = n % 10
    tong += chuso
    dem += 1
    n = n // 10
print(dem)
print(tong)
