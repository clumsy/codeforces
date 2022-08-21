t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    # if palindrome we can max 1 unique string
    # if not palindrome and k > 0 there are always 2 unique strings
    print("1" if k == 0 or s == s[::-1] else "2")
