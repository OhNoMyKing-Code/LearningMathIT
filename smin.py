N = int(input())
min1 = float('inf')
min2 = float('inf')
for _ in range(N):
    a = int(input())
    if a < min1:
        min2 = min1
        min1 = a
    elif min1 < a < min2:
        min2 = a
print(min1, min2)
