mz = int(input())
ma, mb, mc =[], [], []
for i in range(mz):
    a = list(map(int, input().split()))
    ma += a

for i in range(mz):
    b = list(map(int, input().split()))
    mb += b

for i in range(mz**2):
    mc.append(ma[i] + mb[i])

for i in range(len(mc)):
    print(mc[i], end=' ')
    if (i + 1) % mz == 0:
        print('\n', end='')