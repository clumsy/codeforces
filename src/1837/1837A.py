t = int(input())
for _ in range(t):
    x, k = (int(i) for i in input().split())
    res = [x - 1, 1] if x % k == 0 else [x]
    print(len(res))
    print(*res)
