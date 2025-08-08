s = input()
dem = [0] * 256
for i in range(len(s)):
    idx = ord(s[i])
    dem[idx] += 1
cnt = 0
for i in range(0,256):
    if dem[i] == 1:
       cnt += 1
res = s[0]
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        res = res + s[i]
print(cnt)
print(res)