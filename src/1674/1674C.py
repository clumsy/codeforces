t = int(input())
for i in range(t):
    s, t = (input() for _ in range(2))
    res = -1 if len(t) > 1 and "a" in t else 1 if t == "a" else 2 ** s.count("a")
    print(res)
