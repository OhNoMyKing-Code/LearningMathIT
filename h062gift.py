n = int(input())
if n % 2 == 0:
    viet = nam = n // 2
else:
    viet = n // 2
    nam = viet + 1
print(viet, nam)
