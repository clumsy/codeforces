t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = set(int(i) for i in input().split())
    b = set(int(i) for i in input().split())
    res = min(a & b, default=None)
    res = f"YES\n1 {res}" if res is not None else "NO"
    print(res)
