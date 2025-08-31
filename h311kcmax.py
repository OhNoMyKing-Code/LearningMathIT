n = int(input())
p = []
for i in range(n):
    x,y = map(float, input().split())
    p.append((x,y))

tong = 0
for i in range(n-1):
    for j in range(i+1,n):
        xa, ya = p[i]
        xb, yb = p[j]
        dab = ((xa - xb)**2 + (yb-ya)**2)**0.5
        tong = max(tong, dab)
print("%.2f" % tong)

