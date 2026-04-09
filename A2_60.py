n = int(input())
shots = []
for i in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))

for tx in range(1, 1000):
    for ty in range(1, 1000):
        if all((tx-x)**2 + (ty-y)**2 == d**2 for x, y, d in shots):
            print(tx, ty)
            exit()