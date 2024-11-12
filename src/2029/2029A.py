t = int(input())
for _ in range(t):
    l, r, k = (int(i) for i in input().split())
    res = max(0, r // k - l + 1)
    print(res)
