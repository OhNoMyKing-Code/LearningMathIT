n = int(input())
if n <= 1:
    print("NO")
else:
    i = 2
    la_nt = 1
    while i <= n // i:
        if n % i == 0:
            la_nt = 0
            break
        i += 1
    if la_nt == 1:
        print("YES")
    else:
        print("NO")
