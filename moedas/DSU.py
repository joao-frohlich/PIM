class DSU:
    def __init__(self, n):
        self.n = n
        self.sz = [1]*(n+5)
        self.pa = []
        for i in range(0,n+5):
            self.pa.append(i)

    def root(self, a):
        if self.pa[a] != a: self.pa[a] = self.root(self.pa[a])
        return self.pa[a]
    
    def find(self, a, b):
        return self.root(a) == self.root(b)
    
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a != root_b:
            if self.sz[root_a] > self.sz[root_b]: root_a, root_b = root_b, root_a
            self.pa[root_a] = root_b
            self.sz[root_b] += self.sz[root_a]
    
    def tam_conjuntos(self):
        szs = []
        for i in range(0,self.n):
            if self.pa[i] == i:
                szs.append(self.sz[i])
        return szs
