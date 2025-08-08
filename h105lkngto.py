a, b = map(int, input().split())
co_so_nt = False
for n in range(a, b + 1):
    if n < 2:
        continue
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
        i += 1
    if is_prime:
        print(n)
        co_so_nt = True
if not co_so_nt:
    print("NONE")
