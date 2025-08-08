a, b = map(int, input().split())
x = a
y = b
while y != 0:
    r = x % y
    x = y
    y = r
gcd = x
lcm = (a * b) // gcd
print(lcm)
