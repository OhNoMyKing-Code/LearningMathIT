n = int(input())
sv = []
for i in range(n):
    ten, toan, van = map(str,input().split())
    toan = float(toan); van = float(van)
    tb = (toan+van)/2
    sv.append((ten,tb))

sv.sort(key=lambda x: (-x[1], x[0]))
for ten,tb in sv:
    print(ten, "%.2f" %tb)