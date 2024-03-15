t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = 2 if "..." in s else s.count(".")
    print(res)
