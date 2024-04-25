t = int(input())
for _ in range(t):
    s = input()
    res = "A" if s.count("A") >= 3 else "B"
    print(res)
