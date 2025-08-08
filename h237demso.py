def dem(S):
    dem = 0
    for c in S:
        if c.isdigit():
            dem += 1
    return dem
S = input()
kq = dem(S)
print(kq)