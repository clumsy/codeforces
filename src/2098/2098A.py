from collections import Counter


t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(int(c) for c in s)
    res, stk = [], []
    for i in range(10):
        for _ in range(cnt.get(9 - i, 0)):
            stk.append(9 - i)
        res.append(stk.pop())
    res = "".join(str(i) for i in res)
    print(res)
