from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity = self.velocity.rotate(angle) *1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2
        self.radius -= ASTEROID_MIN_RADIUS
        self.spawn(self.radius, self.position, velocity)
        self.spawn(self.radius, self.position, velocity2)

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity