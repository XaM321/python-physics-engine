from __future__ import annotations

class Vec2:
    def __init__(self, x: float, y: float) -> None:
        """
        2D Vector
        Takes x and y coordinates as floats
        Has magnitude, unit vector, dot product, scalar resolute, vector resolute, addition, subtraction
        """
        self.x: float = x
        self.y: float = y

    @classmethod
    def fromTups(cls, a: tuple[float, float], b: tuple[float, float]) -> Vec2:
        return cls(b[0] - a[0], b[1] - a[1])

    @property
    def mag(self) -> float:
        """
        Returns the magnitude of the vector as a float
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @property
    def unit(self) -> Vec2:
        """
        Returns the same vector with a magnitude of one
        """
        return self / self.mag

    def normalL(self) -> Vec2:
        return type(self)(self.y, -self.x)

    def dot(self, other: Vec2) -> float:
        """
        Takes a 2D Vector
        Returns the dot product of the two vectors
        """
        return self.x * other.x + self.y * other.y

    def scalarr(self, other: Vec2) -> float:
        """
        Takes a 2D Vector
        Returns the Scalar Resolute of the two vectors
        """
        return self.dot(other) / other.mag

    def vectorr(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Returns the Vector Resolute of the two vectors
        """
        scalar = self.scalarr(other)
        other_unit = other.unit
        return other_unit * scalar

    def __add__(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Adds the two vectors
        """
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Subtracts the two vectors
        """
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vec2:
        return type(self)(self.x * other, self.y * other)

    def __truediv__(self, other: float) -> Vec2:
        return type(self)(self.x / other, self.y / other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
