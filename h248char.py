s = input()
s=s.lower()
dem = [0]*256
for c in s:
    x = ord(c)
    dem[x] += 1
for x in range(97,122+1):
    if dem[x] > 0:
        print(chr(x), dem[x])