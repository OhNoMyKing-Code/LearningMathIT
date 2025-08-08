a, b, c, d = map(int, input().split())
max_even = -1 
if a % 2 == 0 and a > max_even:
    max_even = a
if b % 2 == 0 and b > max_even:
    max_even = b
if c % 2 == 0 and c > max_even:
    max_even = c
if d % 2 == 0 and d > max_even:
    max_even = d
if max_even == -1:
    print("NONE")
else:
    print(max_even)
