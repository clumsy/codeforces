n = int(input())
for _ in range(n):
    s = input()
    i = len(s) - 1
    while s[i] == "0":
        i -= 1
    res = s[:i]
    print(res)
