n, s = int(input()), input()
p = [
    "vaporeon",
    "jolteon",
    "flareon",
    "espeon",
    "umbreon",
    "leafeon",
    "glaceon",
    "sylveon",
]
res = next(
    c for c in p if len(c) == len(s) and all(i == j or j == "." for i, j in zip(c, s))
)
print(res)
