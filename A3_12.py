n, s = map(int, input().split())

c = [0]
for _ in range(n):
    c.append(int(input()))

visited = [False] * (n + 1)
ans = 0
current = s

while current != 0 and not visited[current]:
    visited[current] = True
    ans += 1
    current = c[current]

print(ans)