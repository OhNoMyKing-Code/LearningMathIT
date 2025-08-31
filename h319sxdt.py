n = int(input())
a = []
for i in range(n):
    L, R = map(int, input().split())
    a.append((L,R))

a.sort(key = lambda x: (-(x[1] - x[0])  , x[0]))

for x in a:
    print(x[0], x[1])