import pygame
import math

from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

PLAYER_RADIUS = 20

class Player(CircleShape):
    def __init__(self, x: int, y: int, *groups):
        super().__init__(x, y, PLAYER_RADIUS, *groups)
        self.rotation = 0
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self._groups = groups
        self.shoot_timer = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.rect.center = (int(self.position.x), int(self.position.y))
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot()

    def update(self, dt):
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            if self.shoot_timer < 0:
                self.shoot_timer = 0.0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        
          
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        shot_start_offset = shot_direction * (self.radius +5)
        shot_start_pos = self.position + shot_start_offset
        Shot(shot_start_pos.x, shot_start_pos.y, shot_velocity,)        
        


        