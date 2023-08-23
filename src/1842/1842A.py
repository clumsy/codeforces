t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    diff = sum(a) - sum(b)
    res = "Draw" if diff == 0 else "Tsondu" if diff > 0 else "Tenzing"
    print(res)
