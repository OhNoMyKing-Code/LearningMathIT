a, b = map(int, input().split())
x = a
y = b
while y != 0:
    r = x % y
    x = y
    y = r
gcd = x
c = a // gcd
d = b // gcd
print(c, d)
