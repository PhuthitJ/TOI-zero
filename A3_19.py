# Haven't fixed yet.

N, L = map(int, input().split())
H = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))
arr = []
tallest = 0
count = 0

for i in range(1, len(H) + 1):
    if i in A and i != 1:
        if H[i - 2] > H[i - 1]:
            H[i - 1] += 1
            count += 1
            tallest = i
        else:
            arr.append(count)

print(arr)
print(A)
print(H)
print(tallest)