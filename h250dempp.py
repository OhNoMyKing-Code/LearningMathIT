s = input()
dem = [0]*256
for x in range(len(s)):
    d = ord(s[x])
    dem[d]+= 1
for i in range(97,123+1):
    if dem[i] != 0:
        print(chr(i),dem[i])