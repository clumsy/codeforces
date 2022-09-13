t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    bs = a.count("b")
    res = "b" * bs + a.replace("b", "")
    print(res)
