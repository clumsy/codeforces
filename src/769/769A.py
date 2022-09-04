_, y = input(), (int(i) for i in input().split())
min_y, max_y = 2101, 2009
for i in y:
    min_y = min(min_y, i)
    max_y = max(max_y, i)
res = (min_y + max_y) // 2
print(res)
