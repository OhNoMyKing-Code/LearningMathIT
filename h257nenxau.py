s = input()
res = ''
dem = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        dem += 1
    else:
        res += s[i-1] + str(dem)
        dem = 1
res += s[-1] + str(dem)
print(res)
