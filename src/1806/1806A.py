t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = -1 if d < b or a + (d - b) < c else d - b + a + (d - b) - c
    print(res)
