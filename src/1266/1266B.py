t = int(input())
for x in (int(i) for i in input().split()):
    # except top dice we always "loose" 7 points out of 21, each dice adds 14
    # for last dice we can get 15-20
    res = "YES" if x > 14 and 1 <= x % 14 <= 6 else "NO"
    print(res)
