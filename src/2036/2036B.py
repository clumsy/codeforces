t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    cnt = [0] * k
    for _ in range(k):
        b, c = (int(i) for i in input().split())
        cnt[b - 1] += c
    cnt.sort()
    res = sum(cnt[-min(n, len(cnt)) :])
    print(res)
