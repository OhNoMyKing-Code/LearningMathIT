x = input()
y = input()
demx = [0] * 256; demy = [0] * 256
for c in x:
    demx[ord(c)] += 1
for c in y:
    demy[ord(c)] += 1

for i in range(256):
    if demx[i] > 0 and demy[i] > 0:
        print(chr(i))