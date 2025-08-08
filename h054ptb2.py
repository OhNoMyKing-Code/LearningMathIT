a, b, c = map(float, input().split())
delta = b * b - 4 * a * c
if delta < 0:
    print("NONE")
elif delta == 0:
    x = -b / (2 * a)
    print("%.2f" % x)
else:
    can = delta ** 0.5
    x1 = (-b + can) / (2 * a)
    x2 = (-b - can) / (2 * a)
    if x1 > x2:
        print("%.2f %.2f" % (x1, x2))
    else:
        print("%.2f %.2f" % (x2, x1))
