t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "STAIR" if a < b < c else "PEAK" if a < b > c else "NONE"
    print(res)
