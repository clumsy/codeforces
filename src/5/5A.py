import sys

res = cnt = 0
for s in sys.stdin:
    if s[0] == "+":
        cnt += 1
    elif s[0] == "-":
        cnt -= 1
    else:
        res += cnt * len(s[s.index(":") + 1 :].strip())
print(res)
