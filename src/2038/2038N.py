t = int(input())
for _ in range(t):
    s = [c if i == 1 else int(c) for i, c in enumerate(input())]
    s[1] = "=" if s[0] == s[2] else "<" if s[0] < s[2] else ">"
    res = "".join(str(c) for c in s)
    print(res)
