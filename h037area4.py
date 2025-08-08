a, b, c = map(float, input().split())
pi = 3.14
h = (c**2 - ((b - a) / 2)**2) ** 0.5
vuon = (a + b) * h / 2
gieng = pi * (h / 4) ** 2
conlai = vuon - gieng
print("%.2f" % conlai)