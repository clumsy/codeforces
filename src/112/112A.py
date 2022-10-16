a, b = input().lower(), input().lower()
res = 0
for i in range(len(a)):
    res = ord(a[i]) - ord(b[i])
    if res != 0:
        res = -1 if res < 0 else 1
        break
print(res)
