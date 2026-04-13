n, d = map(int, input().split())

hashtag = {
    1:"TechTrends",
    2:"EcoLife",
    3:"FoodieHeaven",
    4:"FashionWeek",
    5:"HealthyLiving",
}

ids = []
total = []
avg = []
trend = []

for i in range(n):
    row = list(map(int, input().split()))
    
    current_id = row[0]
    data = row[1:] 
    
    ids.append(current_id)

    if data[-1] > data[0]:
        trend.append("GROWING")
    elif data[-1] < data[0]:
        trend.append("DECLINING")
    else:
        trend.append("STABLE")

    current_total = sum(data)
    total.append(current_total)
    avg.append(current_total / d)

for i in range(n):
    print(f'{hashtag[ids[i]]}: {total[i]} total, {avg[i]:.2f} avg, {trend[i]}')

top_index = total.index(max(total))
print(f'Top performer: {hashtag[ids[top_index]]}')