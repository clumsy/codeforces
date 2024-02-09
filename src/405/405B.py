n = int(input())
s = input()
res = cur = 0
for i, c in enumerate(s):
    if c == ".":
        cur += 1
    elif c == "L":
        res += cur & 1 == 1 and i - cur - 1 >= 0 and s[i - cur - 1] == "R"
        cur = 0
    else:  # c == "R"
        res += cur
        cur = 0
res += cur if cur == len(s) or s[-cur - 1] != "R" else 0
print(res)
