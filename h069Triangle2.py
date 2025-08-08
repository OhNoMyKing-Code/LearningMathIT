a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
