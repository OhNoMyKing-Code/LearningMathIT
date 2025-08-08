N = int(input())
a = N // 100
b = (N // 10) % 10
c = N % 10
max_digit = a
if b > max_digit:
    max_digit = b
if c > max_digit:
    max_digit = c
print(max_digit)
