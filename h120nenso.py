n = int(input())

while n >= 10:
    tong = 0
    while n > 0:
        cs = n % 10
        tong += cs
        n = n // 10
    n = tong

print(n)
