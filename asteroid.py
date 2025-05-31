import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), int(self.radius),  2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        new_asteroids = []
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return new_asteroids

        random_angle = random.uniform(20, 50)

        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if new_radius < 1:
            new_radius = 1

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius, velocity=new_velocity_1 * 1.2)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius, velocity=new_velocity_2 * 1.2)

        new_asteroids.append(new_asteroid_1)
        new_asteroids.append(new_asteroid_2)
        return new_asteroids

        
        # Additional logic for asteroid movement can be added here