t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    res, prev = 1, -1
    for i in a:
        if i == prev == 0:
            res = -1
            break
        elif i == prev == 1:
            res += 5
        elif i == 1:
            res += 1
        prev = i
    print(res)
