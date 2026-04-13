n, d = map(int, input().split())

hashtag = {
    1:"TechTrends",
    2:"EcoLife",
    3:"FoodieHeaven",
    4:"FashionWeek",
    5:"HealthyLiving",
}

total = []
avg = []
trend = []

for i in range(n):
    row = list(map(int, input().split()))

    if row[-1] > row[1]:
        trend.append("GROWING")
    elif row[-1] < row[1]:
        trend.append("DECLINING")
    else:
        trend.append("STABLE")

    total.append((sum(row)) - (i + 1))
    avg.append((sum(row) - (i + 1)) / (len(row) - 1))

for i in range(n):
    print(f'{hashtag[i + 1]}: {total[i]} total, {avg[i]:.2f} avg, {trend[i]}')

print(f'Top performer: {hashtag[total.index(max(total)) + 1]}')