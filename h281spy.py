u,v = map(int, input().split())
n = int(input())
s = input()
x = y = 0; ok = 0
for i in range(n):
    if abs(u-x) <= 1 and abs(v-y) <= 1:
        print(i); ok = 1;
    if s[i] == "U": y += 1
    elif s[i] == "D": y -= 1
    elif s[i] == "L": x -= 1
    else: x += 1

if abs(u-x) <= 1 and abs(v-y) <= 1:
    print(n)
    ok = 1
if ok == 0:
    print(-1)