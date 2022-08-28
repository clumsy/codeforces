t = int(input())
for _ in range(t):
    x = int(input())
    fst = x - (x & (x - 1))  # first set bit
    snd = fst
    if x & (x - 1) == 0:  # only if power of 2 (single bit set)
        snd = ~x - (~x & (~x - 1))  # first set bit of inverse
    print(fst | snd)
