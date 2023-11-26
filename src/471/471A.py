from collections import Counter

a = (int(i) for i in input().split())
cnt = Counter(a)
leg = cnt.most_common(1)[0]
if leg[1] >= 4:
    cnt[leg[0]] -= 4
    if cnt[leg[0]] == 0:
        del cnt[leg[0]]
    res = "Bear" if len(cnt) == 2 else "Elephant"
else:
    res = "Alien"
print(res)
