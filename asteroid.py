# class for creating asteroids
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            theta = random.uniform(20, 50)
            new_vel = [self.velocity.rotate(theta), self.velocity.rotate(-theta)]
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            for i in range(2):
                new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                new_asteroid.velocity = new_vel[i] * 1.2
