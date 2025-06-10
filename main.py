# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import game constants
from constants import (
    #    ASTEROID_KINDS,
    #    ASTEROID_MAX_RADIUS,
    #    ASTEROID_MIN_RADIUS,
    #    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # define groups for organization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update gamestate
        updatable.update(dt)

        # draw gamestate
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
