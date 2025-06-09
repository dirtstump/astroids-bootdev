# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import game constants
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
)

def main():
    
    pygame.init()
    SCREENWIDTH = 800
    SCREENHEIGHT = 800
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    
    while True:
        pygame.draw.rect(screen, RED, (400, 400, 20, 20), 0)
        screen.fill(RED)
        pygame.display.update()
        print("working")
    
def main2():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
