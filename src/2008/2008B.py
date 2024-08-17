t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    k = 2 if s == "1" * 4 else 0 if "0" not in s else s.index("0") - 1
    res = "YES" if n == k * k else "NO"
    if res == "YES":
        for r in range(k):
            for c in range(k):
                if s[r * k + c] != (
                    "1" if r % (k - 1) == 0 or c % (k - 1) == 0 else "0"
                ):
                    res = "NO"
                    break
    print(res)
