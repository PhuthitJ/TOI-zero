A = []
B = []
C = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    A.append(list(map(int, input().split())))

for i in range(3):
    B.append(list(map(int, input().split())))

MOD = (2**15) + 9

for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]
        C[i][j] = ((C[i][j] % MOD) + MOD) % MOD

for i in range(3):
    for j in range(3):
        print(C[i][j], end=' ')
    print()