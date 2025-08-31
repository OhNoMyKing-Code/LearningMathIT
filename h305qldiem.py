n = int(input())
a = []
for i in range(n):
    ten, toan, van = map(str, input().split())
    t = (ten, toan, van)
    a.append(t)

for x in a:
    diem = (int(x[1]) + int(x[2]))/2
    print(x[0], '%.1f'%diem)