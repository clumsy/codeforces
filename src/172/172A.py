n = int(input())
s = [input() for _ in range(n)]
res, i = len(s[0]), 0
while i < res:
    for j in range(1, n):
        if s[j][i] != s[0][i]:
            res = i
            break
    i += 1
print(res)
