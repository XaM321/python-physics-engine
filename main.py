from vector import Vec2
from physics import RectPhysics

import pygame

WIDTH = 1200
HEIGHT = 800
FPS = 180
SCALE = 100
GRAVITY = -9.8

BLACK: tuple[int, int, int] = (0, 0, 0)

running: bool = True
dt: float = 0

box1 = RectPhysics(Vec2(0.5, 5), 1, 1, 100, 0.6, (255, 0, 0), acceleration = Vec2(0, GRAVITY), scale = SCALE, floor = HEIGHT / SCALE)
box2 = RectPhysics(Vec2(8, 5), 0.8, 0.8, 100, 1, (0, 255, 0), velocity = Vec2(-3, 0), acceleration = Vec2(0, GRAVITY), scale = SCALE, floor = HEIGHT / SCALE)

light = Vec2(600, 700)

clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))

def update() -> None:
    win.fill(BLACK)

    tl = Vec2(box2.left, box2.top) - light
    tr = Vec2(box2.right, box2.top) - light
    bl = Vec2(box2.left, box2.bottom) - light
    br = Vec2(box2.right, box2.bottom) - light

    vecs = (tl, tr, bl, br)

    points: list[tuple] = []

    for vec1 in vecs:
        outest = []
        for vec2 in vecs:
            if vec1 == vec2: continue
            outest.append(((vec2.vectorr(vec1)).x < vec1.x) ^ (0 <= vec1.x))

        if any(outest):
            points.append(tuple(vec1 + light))

    if box2.bottom < light.y and box2.right < light.x: # top left
        points = sorted(points, key = lambda val: val[0] - val[1])
        points += [(WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)]
    elif box2.top > light.y and box2.right < light.x: # bottom left
        points = sorted(points, key = lambda val: -val[0] - val[1])
        points += [(0, 0), (WIDTH, 0), (WIDTH, HEIGHT)]
    elif box2.bottom < light.y and box2.left > light.x: # top right
        points = sorted(points, key = lambda val: val[0] + val[1])
        points = [(WIDTH, HEIGHT), (0, HEIGHT), (0, 0)] + points
    elif box2.top > light.y and box2.left > light.x: # bottom right
        points = sorted(points, key = lambda val: -val[0] + val[1])
        points += [(0, HEIGHT), (0, 0), (WIDTH, 0)]
    elif box2.right < light.x: # left
        points = sorted(points, key = lambda val: val[1])
        points += [(WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)]
    elif box2.left > light.x: # right
        points = sorted(points, key = lambda val: val[1])
        points = [(0, HEIGHT), (0, 0)] + points

    if len(points) > 2:
        pygame.draw.polygon(win, (255, 255, 255), points)

    pygame.draw.rect(win, box1.colour, box1.rect)
    pygame.draw.rect(win, box2.colour, box2.rect)
    pygame.draw.rect(win, (255, 255, 255), (light.x, light.y, 10, 10))

    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    box1.tick(dt)
    box2.tick(dt)

    box1.checkCollisions()
    box2.checkCollisions()

    mouse = pygame.mouse.get_pos()

    # box2.pos.x = mouse[0] / SCALE
    # box2.pos.y = (HEIGHT - mouse[1]) / SCALE

    light.x = mouse[0]
    light.y = mouse[1]

    if box2.right >= WIDTH and box2.velocity.x > 0:
        box2.velocity.x = -abs(box2.velocity.x)
    elif box2.pos.x < 0:
        box2.velocity.x = abs(box2.velocity.x)

    dt = clock.tick_busy_loop(FPS) / 1000
