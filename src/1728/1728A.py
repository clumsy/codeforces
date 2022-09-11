t = int(input())
for _ in range(t):
    n, cnt = int(input()), [int(i) for i in input().split()]
    res = 1
    for i in range(1, n):
        # we can always make it so that majority color remains
        if cnt[i] > cnt[res - 1]:
            res = i + 1
    print(res)
