n = int(input())
dem = 0
for i in range(1, n + 1):
    x = i
    so = True
    while x > 0:
        d = x % 10
        if d != 6 and d != 8:
            so = False
            break
        x = x // 10
    if so:
        dem += 1
print(dem)
