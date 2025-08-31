n = int(input())
a = []
for i in range(n):
    ten, diem = map(str, input().split())
    diem = int(diem)
    a.append((ten, diem))

top_name = ''; max_score = -1
for x in a:
    if x[1] > max_score:
        max_score = x[1]
        top_name = x[0]
print(top_name, max_score)