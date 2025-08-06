from itertools import zip_longest


t = int(input())
for _ in range(t):
    n = int(input())
    res = [
        1,
        *(
            i
            for a, b in zip_longest(
                range(3, (n + 1) // 2 + 1), reversed(range((n + 1) // 2 + 1, n + 1))
            )
            for i in (a, b)
            if i
        ),
        2,
    ]
    print(*res)
