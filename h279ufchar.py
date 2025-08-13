def find(s):
    dem = [0] * 256
    for c in s:
        dem[ord(c)] += 1
    for i in range(len(s)):
        if dem[ord(s[i])] == 1:
            return i+1
    return -1

T = int(input())
for _ in range(T):
    s = input()
    print(find(s))