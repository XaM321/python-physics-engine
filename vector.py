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

    def __round(self, val: float) -> float:
        return round(val, 8)

    @property
    def mag(self) -> float:
        """
        Returns the magnitude of the vector as a float
        """
        return self.__round((self.x ** 2 + self.y ** 2) ** 0.5)

    @property
    def unit(self) -> Vec2:
        """
        Returns the same vector with a magnitude of one
        """
        mag = self.mag
        return type(self)(self.__round(self.x / mag), self.__round(self.y / mag))

    def dot(self, other: Vec2) -> float:
        """
        Takes a 2D Vector
        Returns the dot product of the two vectors
        """
        return self.__round(self.x * other.x + self.y * other.y)

    def scalarr(self, other: Vec2) -> float:
        """
        Takes a 2D Vector
        Returns the Scalar Resolute of the two vectors
        """
        return self.dot(other.unit)

    def vectorr(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Returns the Vector Resolute of the two vectors
        """
        scalar = self.scalarr(other)
        other_unit = other.unit
        return type(self)(self.__round(other_unit.x * scalar), self.__round(other_unit.y * scalar))

    def __add__(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Adds the two vectors
        """
        return type(self)(self.__round(self.x + other.x), self.__round(self.y + other.y))

    def __sub__(self, other: Vec2) -> Vec2:
        """
        Takes a 2D Vector
        Subtracts the two vectors
        """
        return type(self)(self.__round(self.x - other.x), self.__round(self.y - other.y))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
