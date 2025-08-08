x1, y1, x2, y2, R = map(float, input().split())
dx = x1 - x2
dy = y1 - y2
d2 = dx * dx + dy * dy
R2 = R * R
if d2 <= R2:
    print("IN")
else:
    print("OUT")
