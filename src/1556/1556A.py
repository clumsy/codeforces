t = int(input())
for _ in range(t):
    c, d = (int(i) for i in input().split())
    # x - y + z = c
    # -x + y + z = d
    # Linear Equation System:
    # x - y + z = c
    #        2z = c + d
    res = -1 if c + d & 1 == 1 else int(c != 0) if c == d else 2
    print(res)
