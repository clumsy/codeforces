t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = max(a[0] * a[1], a[-1] * a[-2])  # max of largest positives and negatives
    print(res)
