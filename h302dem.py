n = int(input())
a = list(map(int, input().split()))
x = int(input())
dem = 0
for i in a:
    if i == x:
        dem += 1
print(dem)