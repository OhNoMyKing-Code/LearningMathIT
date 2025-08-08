n = int(input())
i = 2
tong_max = -1
so1 = -1
so2 = -1
while i * i <= n:
    if n % i == 0:
        j = n // i
        if i != 1 and j != 1 and i != n and j != n:
            tong = i + j
            if tong > tong_max:
                tong_max = tong
                if i < j:
                    so1 = i
                    so2 = j
                else:
                    so1 = j
                    so2 = i
    i += 1
if tong_max == -1:
    print(-1)
else:
    print(so1, so2)
