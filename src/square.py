from src.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError("Square side must be positive")
        super().__init__(side, side)

s = Square(4)
print("\nSQUARE")
print("side:", s.side_a)     # унаследовано от Rectangle
print("area:", s.get_area())
print("perimeter:", s.get_perimeter())