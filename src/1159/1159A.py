n = int(input())
s = input()
res = 0
for c in s:
    if c == "-":
        res = max(0, res - 1)
    else:
        res += 1
print(res)
