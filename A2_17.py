
a, b = map(str, input().split())
data = input().split()
c = data[0]
n = int(data[1]) if len(data) > 1 else None

size = {"S":60, "M":80, "L":100}
price = size[a]
if b == 'T':
    price += 20

if c == 'P':
    price += 15 * n
if c == 'E':
    price += 10 * n

print(price)