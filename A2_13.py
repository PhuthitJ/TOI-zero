km, kmv = map(str, input().split())
t, sweetness, tv = map(str, input().split())

km_table = {"H":5, "O":3, "J":2}

kmcal = km_table[km.upper()] * int(kmv)

R_table = {"1":12, "2":18, "3":25}
T_table = {"1":15, "2":20, "3":30}
M_table = {"1":10, "2":15, "3":20}

if t == "R":
    tcal = R_table[sweetness] * int(tv)
elif t == "T":
    tcal = T_table[sweetness] * int(tv)
elif t == "M":
    tcal = M_table[sweetness] * int(tv)

total_cal = kmcal + tcal

print(total_cal)