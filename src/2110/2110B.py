t = int(input())
for _ in range(t):
    s = input()
    b, res = int(s[0] == "("), "NO"
    for c in s[1:]:
        if b == 0:
            res = "YES"
            break
        b += 1 if c == "(" else -1
    print(res)
