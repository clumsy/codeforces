t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = input()
    a = a.replace(" ", "").lstrip("0").rstrip("0")
    res = "YES" if len(a) <= x else "NO"
    print(res)
