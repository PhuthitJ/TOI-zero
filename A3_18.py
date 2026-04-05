L, N = map(int, input().split())
arr = []
for i in range(1, L + 1):
    arr.append(i * i)
total = sum(arr)
remain = total - N
if remain <= 0:
    print("0")
    

layer = 0
for clw in range(L, 0, -1):
    caplayer = clw * clw

    if remain > 0:
        layer += 1
        remain -= caplayer
    else:
        break

print(layer)