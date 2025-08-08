n = int(input())
so_dau = n
so_nguoc = 0

while n > 0:
    cs = n % 10
    so_nguoc = so_nguoc * 10 + cs
    n = n // 10

if so_dau == so_nguoc:
    print("YES")
else:
    print("NO")
