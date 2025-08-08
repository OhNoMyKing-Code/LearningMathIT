n = int(input())
la_dep = 1
while n > 0:
    cs = n % 10
    if cs != 6 and cs != 8:
        la_dep = 0
    n = n // 10

if la_dep == 1:
    print("YES")
else:
    print("NO")
