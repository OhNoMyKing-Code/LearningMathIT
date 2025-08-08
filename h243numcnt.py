s=input()
dem=[0]*256
for i in range(len(s)):
    idx= ord (s[i])
    dem[idx] += 1
for i in range(48,57+1):
    print(dem[i],end=' ')