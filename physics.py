from __future__ import annotations
from collections.abc import Iterable
from vector import Vec2
from pygame import Rect

class SolidObject:
    def __init__(self, pos: Vec2, width: float, height: float, rotation: float, bouncyness: float, colour: tuple[int, int, int], scale: float, floor: float) -> None:
        self.pos: Vec2 = pos
        self.width: float = width
        self.height: float = height
        self.rotation: float = rotation
        self.bouncyness: float = bouncyness if bouncyness <= 1 else 1
        self.colour: tuple[int, int, int] = colour
        self.scale: float = scale
        self.floor: float = floor

class PhysicsObject(SolidObject):
    def __init__(self, pos: Vec2, width: float, height: float, mass: float, rotation: float, bouncyness: float, colour: tuple[int, int, int], velocity: Vec2, acceleration: Vec2, scale: float, floor: float) -> None:
        super().__init__(pos, width, height, rotation, bouncyness, colour, scale, floor)
        self.mass: float = mass
        self.velocity: Vec2 = velocity
        self.acceleration: Vec2 = acceleration
        
    def tick(self, deltatime: float) -> None:
        self.velocity += self.acceleration * deltatime
        self.pos += self.velocity * deltatime

class RectSolid(SolidObject):
    def __init__(self, pos: Vec2, width: float, height: float, rotation: float, bouncyness: float, colour: tuple[int, int, int], scale: float, floor: float) -> None:
        super().__init__(pos, width, height, rotation, bouncyness, colour, scale, floor)

class RectPhysics(PhysicsObject):
    def __init__(self, pos: Vec2, width: float, height: float, mass: float, bouncyness: float, colour: tuple[int, int, int], rotation: float = 0, velocity: Vec2 | None = None, acceleration: Vec2 | None = None, scale: float = 1, floor: float = 0) -> None:
        if velocity is None:
            velocity = Vec2(0, 0)
        if acceleration is None:
            acceleration = Vec2(0, 0)
        super().__init__(pos, width, height, mass, rotation, bouncyness, colour, velocity, acceleration, scale, floor)
        
    @property
    def rect(self) -> Rect:
        return Rect(self.left, self.top, self.width * self.scale, self.height * self.scale)
    
    @property
    def top(self) -> float:
        return (self.floor - self.pos.y) * self.scale
    
    @property
    def left(self) -> float:
        return self.pos.x * self.scale
    
    @property
    def bottom(self) -> float:
        return (self.floor - self.pos.y + self.height) * self.scale
    
    @property
    def right(self) -> float:
        return (self.pos.x + self.width) * self.scale
    
    def checkCollisions(self) -> None:#, objects: Iterable[RectPhysics]) -> None:
        if self.pos.y <= self.height and self.velocity.y < 0:
            self.velocity.y = abs(self.velocity.y) * self.bouncyness# * other.bouncyness
            
        if abs(self.velocity.y) < 0.1 and self.pos.y < self.height: self.pos.y = self.height