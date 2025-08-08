N = int(input())
if N < 2:
    print("false")
else:
    is_prime = True
    i = 2
    while i * i <= N:
        if N % i == 0:
            is_prime = False
        i += 1
    if is_prime:
        print("true")
    else:
        print("false")
