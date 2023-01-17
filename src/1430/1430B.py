t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    res = sum(a[n - k - 1 : n])  # min will always be 0
    print(res)
