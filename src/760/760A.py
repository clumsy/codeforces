days = {
    2: 28,
    4: 30,
    6: 30,
    9: 30,
    11: 30,
}
m, d = (int(i) for i in input().split())
res = (days.get(m, 31) - 1 + d - 1) // 7 + 1
print(res)
