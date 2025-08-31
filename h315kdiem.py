n = int(input())
p = []
for i in range(n):
    x,y = map(int, input().split())
    p.append((x,y))

x0,y0,k = map(int, input().split())
def dist(t):
    return (t[0] - x0)**2 + (t[1] -y0)**2
for i in range(len(p)):
    t = p[i]; t = (t,dist(t)); p[i] = t
p.sort(key = lambda x: x[1])
for i in range(k):
    x,y = p[i][0]
    print(x,y)