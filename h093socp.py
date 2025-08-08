import math
N = int(input())
c = 0
for i in range(1, N+1):
    if math.sqrt(i) % 1 == 0:
        c = c + 1
print(c)