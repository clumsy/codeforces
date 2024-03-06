import string


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = [[c for c in string.ascii_lowercase]]
    res = []
    for i in a:
        c = cnt[i].pop()
        res.append(c)
        if len(cnt) == i + 1:
            cnt.append([])
        cnt[i + 1].append(c)
    res = "".join(res)
    print(res)
