t = int(input())
for _ in range(t):
    a = sorted(int(i) for i in input().split())
    res = min(a[0], a[1]) * min(a[2], a[3])
    print(res)
