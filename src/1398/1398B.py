t = int(input())
for _ in range(t):
    s = input()
    res = sum(len(p) for p in sorted(s.split("0"))[::-2])
    print(res)
