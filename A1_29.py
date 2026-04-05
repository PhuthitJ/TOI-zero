str = input().lower()
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in str:
    if char in vowel:
        count += 1

print(count)