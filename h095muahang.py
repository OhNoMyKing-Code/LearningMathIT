N, a, b = map(int, input().split())
found = False
for x in range(N // a + 1):
    remain = N - a * x
    if remain % b == 0:
        y = remain // b
        print(x, y)
        found = True
if not found:
    print("NONE")