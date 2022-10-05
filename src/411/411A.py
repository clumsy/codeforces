s = input()
res = (
    len(s) >= 5
    and any(c.islower() for c in s)
    and any(c.isupper() for c in s)
    and any(c.isdigit() for c in s)
)
res = "Correct" if res else "Too weak"
print(res)
