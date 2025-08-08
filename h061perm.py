N = int(input())
a = N // 100
b = (N // 10) % 10
c = N % 10
p1 = a * 100 + b * 10 + c
p2 = a * 100 + c * 10 + b
p3 = b * 100 + a * 10 + c
p4 = b * 100 + c * 10 + a
p5 = c * 100 + a * 10 + b
p6 = c * 100 + b * 10 + a
max_val = p1
if p2 > max_val:
    max_val = p2
if p3 > max_val:
    max_val = p3
if p4 > max_val:
    max_val = p4
if p5 > max_val:
    max_val = p5
if p6 > max_val:
    max_val = p6
print(max_val)
