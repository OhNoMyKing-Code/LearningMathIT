a, b = input().split()
a = int(a)
b = int(b)
so_moi_a = 0
tmp = a
while tmp > 0:
    cs = tmp % 10
    so_moi_a = so_moi_a * 10 + cs
    tmp = tmp // 10
so_moi_b = 0
tmp = b
while tmp > 0:
    cs = tmp % 10
    so_moi_b = so_moi_b * 10 + cs
    tmp = tmp // 10
if so_moi_a > so_moi_b:
    print(so_moi_a)
else:
    print(so_moi_b)
