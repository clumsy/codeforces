t = int(input())
for _ in range(t):
    input()
    a = [int(i) for i in input().split()]
    m = sum(1 for i in a if i & 1 == 0)
    if m > 0:
        x = min((i for i in a if i & 1 == 1), default=None)
        if not x:  # no odd number to fuse all even numbers with

            def first_set_bit(n):
                return n - (n & (n - 1))

            # create a single odd number using the one where first bit is lowest
            # we need less operations to convert it
            x = min(a, key=first_set_bit)
            m -= 1  # not taking x into account anymore
            while x & 1 == 0:
                x >>= 1
                m += 1
    print(m)
