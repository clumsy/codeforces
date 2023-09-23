from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    cnt = Counter(s)
    res = (
        "red"
        if cnt["0"] > 0
        and sum(int(k) * v for k, v in cnt.items()) % 3 == 0
        and any(cnt[d] > (d == "0") for d in ["0", "2", "4", "6", "8"])
        else "cyan"
    )
    print(res)
