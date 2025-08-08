m, n, k = map(int, input().split())
print(sum(x == k for row in [list(map(int, input().split())) for _ in range(m)] for x in row))
