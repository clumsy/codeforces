t = int(input())
for _ in range(t):
    s = input()
    bob = ord(min(s[0], s[-1])) - ord("a") + 1 if len(s) & 1 == 1 else 0
    alice = sum(ord(c) - ord("a") + 1 for c in s) - bob
    print("Bob" if bob > alice else "Alice", abs(alice - bob))
