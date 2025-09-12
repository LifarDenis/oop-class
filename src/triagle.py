from math import sqrt
from src.figure import Figure

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated")
        self.a, self.b, self.c = a, b, c

    def get_perimeter(self) -> float:
        return self.a + self.b + self.c

    def get_area(self) -> float:
        # Формула Герона (единственно универсальная по трём сторонам)
        s = self.get_perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


t = Triangle(13, 14, 15)
print("\nTRIANGLE")
print("sides:", t.a, t.b, t.c)
print("area:", t.get_area())
print("perimeter:", t.get_perimeter())
