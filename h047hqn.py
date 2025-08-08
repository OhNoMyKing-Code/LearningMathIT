import math
a, b, c = map(float, input().split())
d = b*b - 4*a*c
if d < 0:
    print("NO SOLUTION")
elif d == 0:
    x = -b / (2*a)
    print(f"{x:.4f}")
else:
    x1 = (-b - math.sqrt(d)) / (2*a)
    x2 = (-b + math.sqrt(d)) / (2*a)
    if x1 > x2:
        x1, x2 = x2, x1
    print('%.4f' % x1)
    print('%.4f' % x2)
