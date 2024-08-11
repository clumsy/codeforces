s = input()
o, cnt = [], 0
for i, c in enumerate(s):
    o.append((cnt, -i, c))
    cnt += 1 if c == "(" else -1
o.sort()
res = "".join(c for _, _, c in o)
print(res)
