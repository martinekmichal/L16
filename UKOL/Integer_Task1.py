class IntegerSet:
    def __init__(self, elements):
        self.elements = set(elements)
    def soucet(self):
        return sum(self.elements)
    def prumer(self):
        if not self.elements:
            raise ValueError("Prázdná pole")
        return self.soucet() / len(self.elements)
    def maximum(self):
        if not self.elements:
            raise ValueError("Prázdná pole")
        return max(self.elements)
    def minimum(self):
        if not self.elements:
            raise ValueError("Prázdná pole")
        return min(self.elements)