n = int(input())
m = n + 1

while True:
    ok = True
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            ok = False
            break
    if ok:
        print(m)
        break
    m += 1
