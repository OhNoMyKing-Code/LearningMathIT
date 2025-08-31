n = int(input())
product = []
for i in range(n):
    name,price = map(str, input().split())
    price = int(price)
    product.append((name,price))

product.sort(key=lambda x: (x[1], x[0]))
for x in product:
    name, price = x
    print(name, price)