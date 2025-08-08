import math
N = int(input())
uoc = set()
for i in range(1, int(math.isqrt(N)) + 1):
    if N % i == 0:
        uoc.add(i)
        uoc.add(N // i)
for x in sorted(uoc):
    print(x)