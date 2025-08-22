t = int(input())
for _ in range(t):
    s = input()
    res = "T" * s.count("T") + "".join(c for c in s if c != "T")
    print(res)
