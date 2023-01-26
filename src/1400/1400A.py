t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    # 1110000
    # 1110
    #  1100
    #   1000
    #    0000
    # middle element is present in all substrings
    # let us use it in every position for answer
    res = s[n - 1] * n
    print(res)
