t = int(input())
for _ in range(t):

    def regular(s):
        opn, o = s[0], 0
        for c in s:
            if c == opn:
                o += 1
            elif o == 0:
                return False
            else:
                o -= 1
        return o == 0

    s = input()
    res = (
        "YES"
        if s[0] != s[-1]
        and (
            regular(s.replace("A", "B"))
            or regular(s.replace("C", "A"))
            or regular(s.replace("C", "B"))
        )
        else "NO"
    )
    print(res)
