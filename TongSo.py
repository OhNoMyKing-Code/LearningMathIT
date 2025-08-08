n = int(input())
d = 0
for i in range(1,n+1):
    if i % 2 == 0 and i % 5 == 0:
        d = d + i
print(d)