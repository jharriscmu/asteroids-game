import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x: int, y: int, shot_velocity: pygame.math.Vector2, *groups):
        super().__init__(x, y, SHOT_RADIUS, *groups)
        self.velocity = shot_velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius))

    def update(self, dt):
        self.position += (self.velocity * dt)
        # Check if the shot is out of bounds and remove it if so
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()  