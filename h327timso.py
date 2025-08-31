def find_closest(a, x):
    closest = a[0]
    min_diff = abs(a[0] - x)

    for num in a:
        current_diff = abs(num - x)
        if current_diff < min_diff or (current_diff == min_diff and num < closest):
            min_diff = current_diff
            closest = num
    return closest
n,q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(q):
    x = int(input())
    print(find_closest(a, x))
