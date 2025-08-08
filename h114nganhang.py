n, m = map(int, input().split())
nam = 0
while n < m:
    n = n + n // 10
    nam += 1
print(nam)
