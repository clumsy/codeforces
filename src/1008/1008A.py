s = input()
vowels = {"a", "e", "i", "o", "u"}
vowels_or_n = vowels | {"n"}
res = "NO" if s[-1] not in vowels_or_n else "YES"
for i in range(1, len(s)):
    if s[i - 1] not in vowels_or_n and s[i] not in vowels:
        res = "NO"
        break
print(res)
