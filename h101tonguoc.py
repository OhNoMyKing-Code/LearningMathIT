N = int(input())
tong = 0
i = 1
while i <= N:
    if N % i == 0:
        tong += i
    i += 1
print(tong)
