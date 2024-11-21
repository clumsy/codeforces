t = int(input())
for _ in range(t):
    k, a = int(input()), (int(i) for i in input().split())
    cnt = [0] * (k + 1)
    for i in a:
        cnt[i] += 1
    k -= 2
    for n in range(1, k + 1):
        if k % n == 0 and cnt[n] > 0:
            m = k // n
            if cnt[m] > int(n == m):
                res = n, m
                break
    print(*res)
