m, n = map(int, input().split())
print(max(x for row in [list(map(int, input().split())) for _ in range(m)] for x in row))
