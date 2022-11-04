t = int(input())
for _ in range(t):
    s = input()
    res = "".join([s[0]] + [s[i] for i in range(1, len(s), 2)])
    print(res)
