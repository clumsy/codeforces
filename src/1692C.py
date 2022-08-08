t = int(input())
for _ in range(t):
    input()
    b = [[c for c in input()] for r in range(8)]
    for r in range(1, 7):
        for c in range(1, 7):
            if (
                b[r][c]
                == b[r - 1][c - 1]
                == b[r + 1][c - 1]
                == b[r - 1][c + 1]
                == b[r + 1][c + 1]
                == "#"
            ):
                print(r + 1, c + 1)
