a = input()

if len(a) > 1 and a[1].isdigit():
    num = int(a[:2])
    k = a[2]
else:
    num = int(a[0])
    k = a[1]

k = k.upper()

def get_char(k, level):
    if k == '#':
        return '#'
    base = ord(k) - ord('A')
    pos = base + level
    if pos <= 25:
        return chr(ord('A') + pos)
    else:
        over = pos - 25
        return chr(ord('A') + 25 - over)

mid = num // 2

for i in range(num):
    if num % 2 == 0:
        if i < mid:
            dist = mid - 1 - i
        else:
            dist = i - mid
    else:
        dist = abs(i - mid)

    c = get_char(k, dist)
    left = dist
    right = num - 1 - dist

    row = ['-'] * num
    row[left] = c
    if left != right:
        row[right] = c

    print(''.join(row))