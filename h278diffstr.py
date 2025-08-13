def check(L,s):
    n = len(s); a = []
    for i in range(0, n-L+1):
        tmp = s[i:i+L]
        if tmp in a:
            return 0
        a.append(tmp)
    return 1

n = int(input())
s = input()
for L in range(1, len(s)+1):
    if check(L, s):
        print(L); break