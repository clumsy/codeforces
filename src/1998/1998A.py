t = int(input())
for _ in range(t):
    x, y, k = (int(i) for i in input().split())
    for i in range(k // 2):
        print(x + i + 1, y + i + 1)
        print(x - i - 1, y - i - 1)
    if k & 1 == 1:
        print(x, y)
