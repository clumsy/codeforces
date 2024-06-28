t = int(input())
for _ in range(t):
    x = sorted(int(i) for i in input().split())
    res = min(sum(abs(j - i) for i in x) for j in range(x[0], x[-1] + 1))
    print(res)
