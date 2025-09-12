from src.figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a: float, side_b: float):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides must be positive")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self) -> float:
        return self.side_a * self.side_b

    def get_perimeter(self) -> float:
        return 2 * (self.side_a + self.side_b)


r = Rectangle(3, 5)
print("\nRECTANGLE")
print("sides:", r.side_a, r.side_b)
print("area:", r.get_area())
print("perimeter:", r.get_perimeter())