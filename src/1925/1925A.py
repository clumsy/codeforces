from string import ascii_lowercase

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = ascii_lowercase[:k] * n
    print(res)
