t = int(input())
for _ in range(t):
    x, k = (int(i) for i in input().split())
    while True:
        res = str(x)
        if sum(int(d) for d in res) % k == 0:
            break
        x += 1
    print(res)
