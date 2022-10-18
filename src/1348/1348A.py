t = int(input())
for _ in range(t):
    n = int(input())
    # take 2 ** n with +
    # subtract n // 2 other top powers to stop at 2 ** (n // 2)
    # this is a geometric progression
    res = 2 * (2 ** (n // 2) - 1)
    print(res)
