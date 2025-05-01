t = int(input())
for _ in range(t):
    s = input()
    res = "".join(c[0] for c in s.split())
    print(res)
