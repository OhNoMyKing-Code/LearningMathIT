import math
n = int(input())
tong = 0
i = 1
while i * i <= n:
    if n % i == 0:
        if i != n:
            tong += i
        if i != n // i and n // i != n:
            tong += n // i
    i += 1
if tong > n:
    print(1)
else:
    print(0)
