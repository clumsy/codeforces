# 5 3
# 2 4 6 7 9
# 1 3 5
# ABCDE

# ACE
# AE

# BD
# D
t = int(input())
for _ in range(t):
    _, _ = (int(i) for i in input().split())
    a = next(int(i) for i in input().split())
    q = (int(i) for i in input().split())
    res = [min(i, a - 1) for i in q]
    print(*res)
