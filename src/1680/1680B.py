t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res, min_j = True, None
    for i in range(n):
        s = input()
        if res:
            for j, c in enumerate(s):
                if not res:
                    break
                if c == "R":
                    if min_j is None:
                        min_j = j
                    res = min_j <= j
                    break
    print("YES" if res else "NO")
