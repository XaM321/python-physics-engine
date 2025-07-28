from vector import Vec2

class PhysicsObject:
    def __init__(self, pos: Vec2, width: float, height: float, rotation: float, velocity: Vec2) -> None:
        self.pos: Vec2 = pos
        self.width: float = width
        self.height: float = height
        self.rotation: float = rotation

class Rect(PhysicsObject):
    def __init__(self, pos: Vec2, width: float, height: float, rotation: float, velocity: Vec2 | None = None) -> None:
        if velocity is None:
            velocity = Vec2(0, 0)
        super().__init__(pos, width, height, rotation, velocity)
