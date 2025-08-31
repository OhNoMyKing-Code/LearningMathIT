n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    if i > 0 and i < n-1:
        mi = min(abs(x[i] - x[i - 1]), abs(x[i] - x[i + 1]))
    elif i == 0:
        mi = abs(x[i] - x[i + 1])
    else:
        mi = abs(x[i] - x[i - 1])
    ma = max(abs(x[i] - x[0]), abs(x[i] - x[n-1]))
    print(mi, ma)