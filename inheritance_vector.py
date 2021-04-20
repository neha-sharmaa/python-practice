class C2V:
    def __init__(self, i,j):
        self.i = i
        self.j = j
    def __str__(self):
        return f"{self.i}i + {self.j}j"


class C3V(C2V):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}k"



V1 = C2V(1,3)
V2 = C3V(4, 6, 9)
print(V1)
print(V2)