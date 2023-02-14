t = int(input())
for _ in range(t):
    s = input()
    res = min(2, sum(len(i) > 0 for i in s.split("1")))
    print(res)
