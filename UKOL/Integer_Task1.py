class IntegerSet:
    def __init__(self, elements):
        self.elements = set(elements)
    def sum(self):
        return sum(self.elements)
    def mean(self):
        if not self.elements:
            raise ValueError("Prázdné")
        return self.sum() / len(self.elements)
    def maximum(self):
        if not self.elements:
            raise ValueError("Prázdné")
        return max(self.elements)
    def minimum(self):
        if not self.elements:
            raise ValueError("Prázdné")
        return min(self.elements)