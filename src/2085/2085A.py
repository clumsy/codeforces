t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    res = "NO" if (k == 0 and s >= s[::-1]) or len(set(s)) == 1 else "YES"
    print(res)
