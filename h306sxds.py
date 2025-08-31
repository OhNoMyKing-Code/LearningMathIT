n = int(input())
p = []
for i in range(n):
    x,y = map(int, input().split())
    p.append((x,y))

p.sort()
for x in p:
    print(x[0], x[1])