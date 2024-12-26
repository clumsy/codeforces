t = int(input())
for _ in range(t):
    a = input()
    res = "".join("p" if c == "q" else "q" if c == "p" else "w" for c in a[::-1])
    print(res)
