import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pass
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            th = random.uniform(20, 50)
            d1 = self.velocity.rotate(th)
            d2 = self.velocity.rotate(-th)

            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a2 = Asteroid(self.position.x, self.position.y, new_radius)

            a1.velocity = d1 * 1.2
            a2.velocity = d2 * 1.2
