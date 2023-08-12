from collections import Counter

k = int(input())
for _ in range(k):
    k, n = (input() for _ in range(2))
    for d in ["1", "4", "6", "8", "9"]:
        if d in n:
            res = d
            break
    else:
        # 2 3 5 7
        cnt = Counter(n)
        for i in cnt:
            if cnt[i] > 1:
                res = i + i
                break
        else:
            # only one of each: 2, 3, 5, 7
            for d in ["2", "5"]:
                if d in n[1:]:
                    res = n[0] + d
                    break
            else:
                if n[0] == "2" and "1" in cnt:
                    res = "21"
                elif n[0] == "2" and "5" in cnt:
                    res = "25"
                elif n[0] == "2" and "7" in cnt:
                    res = "27"
                elif n[0] == "5" and "1" in cnt:
                    res = "51"
                elif n[0] == "5" and "7" in cnt:
                    res = "57"
                else:
                    raise  # should not happen!
    print(len(res))
    print(res)
