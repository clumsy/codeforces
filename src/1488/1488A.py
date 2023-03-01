t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    times = y // x
    res = sum(int(i) for i in str(times)) + (y - x * times)
    print(res)
