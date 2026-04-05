
base_score = int(input())
bonus_score = int(input())
days_played = int(input())

total_score = base_score + bonus_score

if days_played > 3:
    total_score = total_score * 1.5

final_score = int(total_score)

rank_code = 1

if final_score >= 1500:
    rank_code = 5
elif final_score >= 1000:
    rank_code = 4
elif final_score >= 500:
    rank_code = 3
elif final_score >= 200:
    rank_code = 2
else:
    rank_code = 1

special_code = 0

if rank_code == 5 and days_played >= 7:
    special_code = 99
elif rank_code == 4 and bonus_score > 300:
    special_code = 88
else:
    special_code = 0

print(final_score)
print(rank_code)
print(special_code)