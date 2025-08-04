t = int(input())
for _ in range(t):
    n, j, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res = "NO" if k == 1 and max(a) != a[j - 1] else "YES"
    print(res)
