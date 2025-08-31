n = int(input())
a = []
for i in range(n):
    ten,thang,hoa,thua = map(str, input().split())
    diem = int(thang) * 3 + int(hoa)
    hieu = int(thang) - int(thua)
    a.append((ten,diem,hieu))

a.sort(key = lambda x: (-x[1], -x[2], x[0]))
for x in a:
    print(x[0])