A, B = map(int, input().split())

for i in range(A, B + 1):
    if i < 2:
        continue

    check = True
    j = 2
    while j * j <= i:
        if i % j == 0:
            check = False
            break
        j += 1

    if check:
        print(i, end=' ')
