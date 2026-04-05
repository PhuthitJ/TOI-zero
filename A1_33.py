n = int(input())
chars = []
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for i in range(n):
    chars.append(input().lower())

for char in chars:
    if char in vowels:
        count += 1

print(count)