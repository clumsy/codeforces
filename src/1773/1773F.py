n, s, c = (int(input()) for _ in range(3))
if n == 1:
    print(f"{int(s == c)}", f"{s}:{c}", sep="\n")
else:
    res = max(0, n - s - c)
    print(res)
    for _ in range(res):
        print("0:0")
    n -= res
    s_won = max(0, min(n - 2 + int(c == 0), s))
    for _ in range(s_won):
        print("1:0")
    n -= s_won
    s -= s_won
    if s:
        print(f"{s}:0")
        n -= 1
    c_won = max(0, min(n - 2 + int(s == 0), c))
    for _ in range(c_won):
        print("0:1")
    c -= c_won
    if c:
        print(f"0:{c}")
