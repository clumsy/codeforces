t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    odd = sum(1 for i in a if i & 1 == 1)
    res = "YES" if odd & 1 == 1 or 1 <= odd < n else "NO"
    print(res)
