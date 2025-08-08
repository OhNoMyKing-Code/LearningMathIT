n = int(input())
i = 1
dem = 0
while i * i <= n:
    dem += 1
    i += 1

print(dem)

i = 1
while i * i <= n:
    print(i * i, end=" ")
    i += 1
