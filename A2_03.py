n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(1, n - 1):
    if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
        count += 1
if arr[0] > arr[1]:
    count += 1
if arr[-1] > arr[-2]:
    count += 1

print(count)
