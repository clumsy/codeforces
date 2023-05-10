t = int(input())
for _ in range(t):
    n, a = int(input()), input().split()
    res, cnt = "YES", {}
    for i in a:
        other = cnt.get(len(i), None)
        if other is None:
            cnt[len(i)] = i
        elif i != other[::-1]:
            res = "NO"
            break
    print(res)
