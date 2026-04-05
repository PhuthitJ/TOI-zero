w, h, m, n = map(int, input().split())
cut_x = input().split()
cut_y = input().split()

cut_x = [0] + list(map(int, cut_x)) + [w]
cut_y = [0] + list(map(int, cut_y)) + [h]

widths = []
for i in range(len(cut_x) - 1):
    size = cut_x[i + 1] - cut_x[i]
    widths.append(size)

heights = []
for i in range(len(cut_y) - 1):
    size = cut_y[i + 1] - cut_y[i]
    heights.append(size)

widths.sort()
heights.sort()

max_area = widths[-1] * heights[-1]

option1 = widths[-1] * heights[-2]
option2 = widths[-2] * heights[-1]

second_max_area = max(option1, option2)

print(f"{max_area} {second_max_area}")