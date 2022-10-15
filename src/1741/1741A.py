t = int(input())
for _ in range(t):
    a, b = input().split()

    def to_int(s):
        return len(s) * (-1 if s[-1] == "S" else 1 if s[-1] == "L" else 0)

    a, b = to_int(a), to_int(b)
    res = "=" if a == b else ">" if a > b else "<"
    print(res)
