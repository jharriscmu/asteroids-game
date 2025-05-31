# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import*
from player import*

BLACK = (0, 0, 0)

def main():
    pygame.init()
    # Initialize the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    all_the_shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (all_the_shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.handle_input(event)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        
        for shot in list(all_the_shots):
            for asteroid in list(asteroids):
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    break

        screen.fill(BLACK)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

