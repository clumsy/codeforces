def solve(m: str, s: str):
    m = {c: i for (i, c) in enumerate(m)}
    return (sum(abs(m[s[i]] - m[s[i - 1]])) for i in range(1, len(s)))


for _ in range(int(input())):
    print(solve(input(), input()))
