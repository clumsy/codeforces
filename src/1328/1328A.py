t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = b - (a % b) if a % b != 0 else 0
    print(res)
