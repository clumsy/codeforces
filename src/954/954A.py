n, s = int(input()), input()
res, i = n, 1
while i < n:
    if s[i] != s[i - 1]:
        res -= 1
        i += 2
    else:
        i += 1
print(res)
