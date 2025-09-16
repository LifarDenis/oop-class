#Квадрат
from src.rectangle import Rectangle  # импортируем класс Rectangle, от которого будем наследовать

# создаём класс Square (Квадрат), он наследуется от Rectangle
class Square(Rectangle):
    def __init__(self, side: int):  # в конструкторе квадрату достаточно одной стороны
        if side <= 0:  # проверка, что сторона положительная
            raise ValueError(f'Сторона квадрата не может быть отрицательной {side}')
        super().__init__(side, side)   # вызываем конструктор Rectangle, передаём две одинаковые стороны
        self.name = "Square"  # переопределяем имя фигуры

# --- пример использования ---

s = Square(5)           # создаём объект квадрата со стороной 5
print(s.perimeter)    # вызываем метод из Rectangle -> 2 * (5 + 5) = 20
print(s.area)         # вызываем метод из Rectangle -> 5 * 5 = 25
