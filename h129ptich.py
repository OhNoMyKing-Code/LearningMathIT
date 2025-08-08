N = int(input())
count = 0
for a in range(0, N // 2 + 1):
    b = N - a
    if a < b:
        count += 1
print(count)
