from itertools import zip_longest

n = int(input())
if n <= 4:
    res = [1] if n < 3 else [1, 3] if n < 4 else [3, 1, 4, 2]
else:
    half = (n + 1) // 2
    res = [
        e
        for f, s in zip_longest(
            range(1, half + 1), range(half + 1, n + 1), fillvalue=None
        )
        for e in (f, s)
        if e
    ]
print(len(res))
print(*res)
