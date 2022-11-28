n = int(input())
m = [input() for _ in range(n)]
res = 0
if n > 2:
    for r in range(1, n - 1):
        for c in range(1, n - 1):
            if (
                m[r][c]
                == "X"
                == m[r - 1][c + 1]
                == m[r - 1][c - 1]
                == m[r + 1][c + 1]
                == m[r + 1][c - 1]
            ):
                res += 1
print(res)
