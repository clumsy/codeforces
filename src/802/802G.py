s = input()
h = "heidi"
j = len(h) - 1
for i in reversed(range(len(s))):
    if s[i] == h[j]:
        j -= 1
        if j < 0:
            break
res = "YES" if j < 0 else "NO"
print(res)
