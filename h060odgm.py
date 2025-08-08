N = int(input())
max_odd = -1 
a = N // 1000
b = (N // 100) % 10
c = (N // 10) % 10
d = N % 10
if a % 2 == 1 and a > max_odd:
    max_odd = a
if b % 2 == 1 and b > max_odd:
    max_odd = b
if c % 2 == 1 and c > max_odd:
    max_odd = c
if d % 2 == 1 and d > max_odd:
    max_odd = d
if max_odd == -1:
    print("NONE")
else:
    print(max_odd)
