t = int(input())
for _ in range(t):
    s = input()
    res = sum(i != j for i, j in zip(s, "codeforces"))
    print(res)
