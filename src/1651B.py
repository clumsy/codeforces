t = int(input())
for _ in range(t):
    n = int(input())
    if 3 ** (n - 1) > 10**9:
        print("NO")
    else:
        # let ai > aj, then ai + aj >= 2*|ai - aj| => ai >= 3*aj
        res = (3**i for i in range(n))
        print("YES"), print(*res)
