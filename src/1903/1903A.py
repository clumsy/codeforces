t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res = "YES" if k > 1 or a == sorted(a) else "NO"
    print(res)
