t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    res = max(len(i) for i in a.replace(" ", "").split("1"))
    print(res)
