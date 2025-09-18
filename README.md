.
├─ src/
│  ├─ figure.py       # абстрактный класс Figure (контракт + add_area)
│  ├─ rectangle.py    # Rectangle(side_a, side_b)
│  ├─ square.py       # Square(side)  ← наследуется от Rectangle
│  ├─ circle.py       # Circle(radius) с PI-константой
│  └─ triangle.py     # Triangle(a, b, c) с формулой Герона
└─ README.md


## Что реализовано

- **Figure**
  - `get_area() -> float` — абстрактный метод.
  - `get_perimeter() -> float` — абстрактный метод.
  - `add_area(other: Figure) -> float` — проверяет тип и возвращает сумму площадей.
- **Rectangle(side_a, side_b)**
  - Валидация: стороны `> 0`.
  - Площадь: `a * b`.
  - Периметр: `2 * (a + b)`.
- **Square(side)**
  - Наследуется от `Rectangle`, конструктор вызывает `super().__init__(side, side)`.
- **Circle(radius)**
  - Валидация: `radius > 0`.
  - Константа `PI` внутри класса.
  - Площадь: `PI * r^2`.
  - Периметр: `2 * PI * r`.
- **Triangle(a, b, c)**
  - Валидация: стороны `> 0` и неравенство треугольника.
  - Периметр: `a + b + c`.
  - Площадь: формула **Герона**.

> Внутри `src/` нет `print` и закомментированного кода (соответствие ТЗ).

---

## Примеры использования

```python
from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle

r = Rectangle(3, 5)      # area = 15, perimeter = 16
s = Square(4)            # area = 16, perimeter = 16
c = Circle(2)            # area ≈ 12.566, perimeter ≈ 12.566
t = Triangle(13, 14, 15) # area = 84.0, perimeter = 42

print("RECTANGLE", r.get_area(), r.get_perimeter())
print("SQUARE   ", s.get_area(), s.get_perimeter())
print("CIRCLE   ", c.get_area(), c.get_perimeter())
print("TRIANGLE ", t.get_area(), t.get_perimeter())

print("SUM (t + s):", t.add_area(s))  # 84 + 16 = 100.0
