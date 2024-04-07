t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = [0] * 3
    for i in a:
        cnt[i % 3] += 1
    c1, c2 = cnt[1:]
    if (c1 + 2 * c2) % 3 == 0:
        res = 0
    elif c1 == 0:
        res = c2 % 3
    else:
        res = 1
    print(res)
