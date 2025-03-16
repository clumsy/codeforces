t = int(input())
for _ in range(t):
    s = input()
    res = len(s)
    for i in range(1, res):
        if s[i] == s[i - 1]:
            res = 1
            break
    print(res)
