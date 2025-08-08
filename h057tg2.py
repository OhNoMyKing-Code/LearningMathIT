x1, y1, x2, y2, x3, y3 = map(int, input().split())
S = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
if S == 0:
    print("NONE")
else:
    print("%.2f" % S)
