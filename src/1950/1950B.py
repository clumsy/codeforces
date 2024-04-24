t = int(input())
for _ in range(t):
    n = int(input())
    for r in range(2 * n):
        for c in range(2 * n):
            print("#" if (r // 2) & 1 == (c // 2) & 1 else ".", end="")
        print()
