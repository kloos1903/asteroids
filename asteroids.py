import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle1 = self.velocity.rotate(random.uniform(20, 50))
        angle2 = self.velocity.rotate(-random.uniform(20,50))
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = angle1 * 1.2
        asteroid2.velocity = angle2 * 1.2

