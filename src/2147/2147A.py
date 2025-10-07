t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    if x < y:
        res = 2
    elif x - 1 > y and y > 1:
        res = 3  # 1, y, y + 1
    else:
        res = -1
    print(res)
