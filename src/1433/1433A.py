t = int(input())
for _ in range(t):
    x = input()
    res = 10 * (int(x[0]) - 1) + (1 + len(x)) * len(x) // 2
    print(res)
