s, t = (input() for _ in range(2))
vowels = "aeiou"
res = (
    "YES"
    if len(s) == len(t)
    and all(c1 == c2 or ((c1 in vowels) == (c2 in vowels)) for c1, c2 in zip(s, t))
    else "NO"
)
print(res)
