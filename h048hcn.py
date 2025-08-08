import math
L = float(input())
S = float(input())
P = L / 2
d = P * P - 4 * S
x1 = (P - math.sqrt(d)) / 2
x2 = (P + math.sqrt(d)) / 2
if x1 > x2:
    x1, x2 = x2, x1
print('%.2f' % x1)
print('%.2f' % x2)
