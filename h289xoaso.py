def append(n,s):
    for x in s:
        n = n + [x]
    return n
p, k = map(int,input().split())
n = []
for i in range(p):
    a,s = map(int,input().split())
    s = str(s)
    for j in range(a):
        n = append(n,s)
n1 = ""
i = 0
while i < len(n):
    if i < len(n1)-1 and n1[i] > n1[i+1]:
        n1.remove(n1[i])
    else:
        i+=1
while dem < k:
    n1.remove(n1[0])
    dem+=1

print("".join(n1))