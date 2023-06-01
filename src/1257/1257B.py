t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if x >= y or (x > 1 and y <= 3) or x > 3 else "NO"
    print(res)
