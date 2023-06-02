q = int(input())


class UnionFind:
    def __init__(self, n):
        self.prnt = [i for i in range(n)]
        self.size = [1] * n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.size[pi] <= self.size[pj]:
                pi, pj = pj, pi
            self.prnt[pj] = pi
            self.size[pi] += self.size[pj]

    def find(self, i):
        if self.prnt[i] != i:
            self.prnt[i] = self.find(self.prnt[i])
        return self.prnt[i]


for _ in range(q):
    n, p = int(input()), [int(i) for i in input().split()]
    uf = UnionFind(n)
    for i in range(n):
        uf.union(i, p[i] - 1)
    res = [uf.size[uf.find(i)] for i in range(n)]
    print(*res)
